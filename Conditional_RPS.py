# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

def rock_paper_scissors():
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == "r" and user_choice == "s":
        print("The computer wins!")
    elif computer_choice == "p" and user_choice == "r":
        print("The computer wins!")
    elif computer_choice == "s" and user_choice == "p":
        print("The computer wins!")
    elif user_choice != "r" and user_choice != "p" and user_choice != "s":
        print("That is not a valid choice.")
        rock_paper_scissors()
    else:
        print("Congratulations! You win!")

rock_paper_scissors()