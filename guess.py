#!/usr/bin/env python

import random

# implement a guess a number game within a range

print ("+++++++++++++++++++++++++++++++++++")
print ("Welcome to the guess a number game!")
print ("+++++++++++++++++++++++++++++++++++")
print ("")
print ("")
random_num = random.choice(range(1,11))
while (True):
    guess = str(input("Guess a number between 1 and 10  >"))
    if not guess.isdigit():
        continue
    else:
        guess = int(guess)

    if guess == random_num:
        print ("You win!!!")
        break



