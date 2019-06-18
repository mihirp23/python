## Mihir Patel
## File: rock_paper_scissors.py
## 6/18/19
## Rock-Paper-Scissors game where user goes
## against the "computer"

import random

POSSIBLE_CHOICES = ["rock", "paper", "scissors"]

user_choice=""
while user_choice not in POSSIBLE_CHOICES:
    user_choice = input("rock, paper, scissors ").lower()
    
computer_choice = POSSIBLE_CHOICES[random.randint(0,2)]

print("     You selected: " + user_choice)
print("Computer selected: " + computer_choice)

if user_choice == computer_choice:
    print("tie")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("computer wins!")
    else:
        print("you win!")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("computer wins!")
    else:
        print("you win!")
        
