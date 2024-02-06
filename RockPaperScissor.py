import random

#Function to evaluate the choices
def game(comp, player):
    if comp == player:
        return None
    if comp == "r" and player == "p":
        return True   
    if comp == "p" and player == "s":
        return True
    if comp == "s" and player == "r":
        return True
            
    return False

#main 
while True:
    opt=['r', 'p', 's']

    #comuter's choice
    comp=random.choice(opt)  

    #player's choice
    player = input("Enter your choice:- rock(r), paper(p) or scissor(s): ")
    while player not in opt:
        player=input("Please enter valid input:- rock(r), paper(p) or scissor(s): ")

    #evaluate
    x = game(comp, player)

    #display of results
    print("Computer chose: " +comp)
    if x == None:
        print("Its a Tie ")
    elif x:
        print("You won!!! :)")
    else:
        print("You lose :(")

    #take user's consent to exit game
    y=bool(input("Enter to continue else enter any letter to exit: "))
    if y:
        break
    