board1 = [
['X','X','O'],
['X','X','O'],
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
        
def get_winner(board):
    for r in range(0,3):
        if all({z == 'X' for z in board[r]}):
            winner = 'X'
            return winner 
#vertical 
    else:
        for r in range( 0, 3):
            if r == 0:
                for c in range (0,3):
                    if board[r+1][c]== 'X' and board[r+2][c] == 'X' and board[r][c] == 'X':   
                        winner = 'X'
                        return winner
            elif r == 1:
                for c in range (0,3):
                    if board [r - 1][c] == 'X' and board[r + 1][c] == 'X' and board[r][c] == 'X':
                        winner = 'X'
                        return winner
            elif r == 2:
                for c in range (0,3):
                    if board[r- 1][c]== 'X' and board[r- 2][c] == 'X'and board[r][c] == 'X':
                        winner = 'X'
                        return winner
#diagonal check
    r , c = 1 , 1
    if board[r+1][c+1]== 'X' and board[r-1][c-1] == 'X' and board[r][c] == 'X': 
        winner = 'X'
        return winner
    elif board[r-1][c+1]== 'X' and board[r+1][c-1] == 'X'and board[r][c] == 'X':
        winner = 'X'
        return winner
#horizontal            
    r , c = 0 , 0
    for r in range(0,3):
        if all({z == 'O' for z in board[r]}):
            winner = 'O'
            return winner 
#vertical 
    else:
        for r in range( 0, 3):
            if r == 0:
                for c in range (0,3):
                    if board[r][c]== 'O' and board[r+1][c] == 'O'and board[r+2][c] == 'O':    
                        winner = 'O'
                        return winner
            elif r ==1:
                for c in range (0,3):
                    if board[r][c]== 'O' and board[r+1][c] == 'O'and board[r - 1 ][c] == 'O':
                        winner = 'O'
                        return winner
            elif r == 2:
                for c in range (0,3):
                    if board[r-2][c]== 'O' and board[r-1][c] == 'O'and board[r][c] == 'O':
                        winner = 'O'
                        return winner
#diagonal check
    r , c = 1 , 1
    if board[r+1][c+1]== 'O' and board[r-1][c-1] == 'O' and board[r][c] == 'O': 
        winner = 'O'
        return winner
    elif board[r-1][c+1]== 'O' and board[r+1][c-1] == 'O'and board[r][c] == 'O':
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
