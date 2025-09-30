import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
youchoice=input("Enter your choice(s for snake, w for water, g for gun): ").lower()
youDict={"w":-1,"s":1,"g":0}
reverseDict={-1:"Water",1:"Snake",0:"Gun"}
if youchoice not in youDict:
    print("Enter a valid choice!")
else:
    you=youDict[youchoice]

    print(f"You chose {reverseDict[you]}\nThe Computer chose {reverseDict[computer]}")

    if(computer==you):
        print("It's a draw")
    elif(computer== -1 and you==0):
        print("You lose!")
    elif(computer== -1 and you==1):
        print("You win!")
    elif(computer== 0 and you==-1):
        print("You win!")
    elif(computer== 0 and you==1):
        print("You lose!")
    elif(computer== 1 and you==0):
        print("You win!")
    elif(computer== 1 and you==-1):
        print("You lose!")
    else:
        print("There is an error!")

#Shorter version in snake_shortened.py