rps = {"rock":{"rock":"tie", "paper":"lose", "scissors":"win"}, "paper":{"paper":"tie", "rock":"win", "scissors":"lose"}, "scissors":{"scissors":"tie", "paper":"win", "rock":"lose"}}

# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice == "s":
        user_choice = "scissors"
    try:
        print("You chose " + user_choice + ". The computer chose " + computer_choice + ". You " + rps[user_choice][computer_choice] + ".")
        play_again = input("Would you like to play again? y/n ")
        if play_again == "y":
            rock_paper_scissors()
    except:
        print("Please make a valid choice.")
        rock_paper_scissors()

rock_paper_scissors()