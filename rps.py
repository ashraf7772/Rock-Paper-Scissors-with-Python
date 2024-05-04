import random

pscore = 0 #player score
cscore = 0 #computer score
opt = ["rock", "paper", "scissors"]


while True:
    pInput = input("Type Rock/Paper/Scissors or Q to quit").lower()
    if pInput == "q": 
        break
    
    if pInput not in opt:
        continue

    rand = random.randint(0, 2) #rock is 0, paper is 1, and scissors is 2
    cChoice = opt[rand]
    print("The computer chose", cChoice)

    if pInput == "rock" and cChoice == "scissors":
        print("You Won")
        pscore += 1

    elif pInput == "scissors" and cChoice == "paper":
        print("You Won")
        pscore += 1

    elif pInput == "paper" and cChoice == "rock":
        print("You Won")
        pscore += 1

    else:
        print("You lost, computer wins")
        cscore +=1

print("Your score is", pscore)
print("The computer score is", cscore)
print("bye")


