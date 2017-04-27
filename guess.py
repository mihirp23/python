#!/usr/bin/env python

import random

###################################################################
# Author : Mihir Patel
#   Date : April 26, 2017
#   Desc : implement an interactive  "Guess a number" game.
###################################################################

print ("+++++++++++++++++++++++++++++++++++")
print ("Welcome to the guess a number game!")
print ("+++++++++++++++++++++++++++++++++++")
print ("")
print ("")

LOW=1
HI=11
random_num = random.choice(range(LOW,HI))

# keep asking the user until the right guess is provided
while (True):
    guess = str(input("Guess a number between 1 and 10  >"))

    # handle invalid input
    if not guess.isdigit():
        print ("Invalid input...You Lose!!!")
        break

    guess = int(guess)
    if guess < random_num:
        print ("Too Low...")
        print ("Try again!")
    elif guess > random_num:
        print ("Too high...")
        print ("Try again!")
    else:
        print ("You win!!!")
        break



