patient0= input("Enter Initial Infected ");
infectedlist = [ patient0 ];
iL = len(infectedlist);
def checkInfected(c):
        if c in infectedlist:
            return True
        return False
#End
bool = True    
while bool: 
    movement = input("Enter Movement String ");
    mL = len(movement);
    newinfected=[]
    for j in range ( 0, mL - 1 ):
        if checkInfected(movement[j]):
            if j != 0:
                newinfected.append(movement[j - 1])
            if j != mL - 1 :
                newinfected.append(movement[j + 1])
    infectedlist = infectedlist + newinfected
    infectedlist = list(dict.fromkeys(infectedlist))
    cont = input("Continue Tracking? ")
    if cont.lower() == "yes":
        continue
    else:
        bool = False
        
print("Here are the infected")
print(infectedlist)
        



        


