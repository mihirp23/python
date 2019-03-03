#!/usr/bin/env python3

## Mihir Patel
## 3/3/19
## Guess a number a game

import random
#################################################################
def main():
#################################################################

    print("Welcome to my game of 'Guess a Number'")
    MAX = 10
    MIN = 1
    # generate random number between a range 
    random_number = random.randint(MIN,MAX)
    while(True):
        # interactively engage user with each guess
        guess = input("guess a number from 1 to 10 : ")
        if guess.isdigit():
            print(random_number)
            guess = int(guess)
            if guess < MIN or guess > MAX:
                print("Outside specified range, try again!")
            elif guess == random_number:
                print("You guessed right! Congrats")
                break
            elif guess > random_number:
                print("guess is high, try again")
            else:
                print("guess is low, try again")
        else:
            print("Invalid input, try again!")
# main()

if __name__ == "__main__":
    main()
