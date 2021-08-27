#-------------ROCK PAPER SCISSORS GAME-------------------------------
""" import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissors: ").lower()


    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("It's a TIE!!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU LOSE!!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU WIN!!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU LOSE!!")
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU WIN!!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU LOSE!!")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Well... YOU WIN!!")

    playAgain = input("Would you like to play again? (yes/no): ").lower()
    if playAgain != "yes":
        break
print("Bye, then! Come back soon!") """