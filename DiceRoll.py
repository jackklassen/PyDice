#PyDice
#Dice roll simulator
#nul


#roll dice
#call random 1 to 6
#    print(random.randint(0,6))
#print output


import random
#random docs: https://docs.python.org/3.1/library/random.html#random.randint

#promt the user to roll wiht infinite while loop
Exit = '0'
while(Exit <= 1):
    NumOfSides = input("enter the number of sides the die has. ") #back option?
    #get the dice side number

    Roll = raw_input("press enter to roll the dice or enter e to exit.")
    if(Roll == 'e'):
        Exit = 1
        break

    Print(RandRoll)

def RandRoll(NumOfSides):
    DiceFace =  random.randint(0,NumOfSides)
#return to orignial loop
    return(DiceFace)
