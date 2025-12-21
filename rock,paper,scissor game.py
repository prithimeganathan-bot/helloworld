import random
while True:
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)
    player = 0
    while player not in choices:
        player = input("Enter rock, paper, or scissor: ").lower()
    if player==computer:
        print("computer:",computer)
        print("player:",player)
        print("oh! It's a tie!")
    elif player=="rock":
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("ohoho! you lose :(")
        if computer=="scissor":
            print("computer:",computer)
            print("player:",player)
            print("heyy! you win :)")
    elif player=="paper":
        if computer=="scissor":
            print("computer:",computer)
            print("player:",player)
            print("ohoho! you lose :(")
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("heyy! you win :)")
    elif player=="scissor":
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("ohoho! you lose :(")
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("heyy! you win :)")

    play_again=input("Do you want to play again? (yes/no): ").lower()
    if play_again!="yes":
        break
print("Bye Bye Have a great day!! :)")

