board1 = [
['X','X','O'],
['O','X','O'],
['O',' ','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
[' ','O','X'],
]

board3 = [
['O','X','O'],
[' ','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O',' ','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X',' ','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X',' ',' '],
]
winner = 'None'

def get_blank (board):
    c = 0
    bc = 0 #blank count
    p = 0
    q = 0
    while c < 3:
        for r in range (0, 3):
            if board[r][c] == ' ':
                bc += 1
                p = r
                q = c
        c += 1
    if bc == 1:
        return p , q  , True
    else :
        return p, c, False
def get_winner(board):
    b = board
    r, c, bool = get_blank(b)
    if bool == False:
        return "None"
    board[r][c] = 'X' 
    if all({z =='X' for z in range(0, r)}):
        winner = 'X'
    else:
        if r == 1:
            if board[r + 1][c]== 'X' and board[r - 1][c] == 'X':
                winner = 'X'
                return winner
                
        elif r == 0:
            if board[r+1][c]== 'X' and board[r+2][c] == 'X':
                winner = 'X'
                return winner
        elif r == 2:
            if board[r-1][c]== 'X' and board[r-2][c] == 'X':
                winner = 'X'
                return winner
    #diagonal check
    if r == 1 and c == 1:
        if board[r+1][c+1]== 'X' and board[r-1][c-1] == 'X' : 
            winner = 'X'
            return winner
        elif board[r-1][c+1]== 'X' and board[r+1][c-1] == 'X':
            winner = 'X'
            return winner
    board[r][c] = 'O'
    if all({z =='O' for z in range(0, r)}):
        winner = 'O'
    #vertical check
    else:
        if r == 1:
            if board[r+1][c]== 'O' and board[r-1][c] == 'O':
                winner = 'O'
                return winner
        elif r == 0:
            if board[r+1][c]== 'O' and board[r+2][c] == 'O':
                winner = 'O'
                return winner
        elif r == 2:
            if board[r-1][c]== 'O' and board[r-2][c] == 'O':
                winner = 'O'
                return winner
    #diagonal check
    if r == 1 and c == 1:
        if board[r+1][c+1] == 'O' and board[r-1][c-1] == 'O':
            winner = 'O'
            return winner
        elif board[r-1][c+1]=='O' and board[r+1][c-1] == 'O':
            winner = 'O'
            return winner 
    
XD= int(input("Enter Board Number: "))
if XD == 1:
    winner = get_winner(board1)
elif XD == 2:
    winner = get_winner(board2)
elif XD == 3:
    winner = get_winner(board3)
elif XD == 4:
    winner = get_winner(board4)
elif XD == 5:
    winner = get_winner(board5)
elif XD == 6:
    winner = get_winner(board6)
print("The winner is" , winner)
