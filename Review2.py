import random
randomNumber = 1
guessaNum = 0
#print (randomNumber)
#def numFun():
while randomNumber != guessaNum:
    randomNumber = random.randint(0,9)
    guessaNum = int(input ("Guess a number !"))
    print (randomNumber)


    if guessaNum == randomNumber:
        print( "Congrats ur done!" )
        break



# Also could make the  input stop and say wrong num if numbe ranything over or under 0 and 9
# first correctional print



# This line also need to print the correct number......it is excluded for some reason
# I want first line to ALSO show correct num...sooooo......ALL YOU !
