#PyDice
#Dice roll simulator
#nul


#roll dice
#call random 1 to 6
#    print(random.randint(0,6))
#print output


import random

#promt the user to roll with an infinite while loop

def RandRoll(NumOfSides):
    DiceFace =  random.randint(0,NumOfSides)
#return to orignial loop
    return(DiceFace)

Exit = 0
while(Exit <= 1):
    NumOfSides = input("enter the number of sides the die has. ") #back option?
    #get the dice side number

    Roll = input("press enter to roll the dice or enter e to exit. ")
    if(Roll == 'e'):
        Exit = 1
        break

    RolledNum =  RandRoll(int(NumOfSides));
    print(RolledNum);

def RandRoll(NumOfSides):
    DiceFace =  random.randint(1,NumOfSides)
#return to orignial loop
    return(DiceFace);
