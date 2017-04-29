#!/usr/bin/env python

import sys

#####################################################################
# Author : Mihir Patel
#   Date : April 29, 2017
#   Desc : calculate the factorial of a number provided by the user.
#          factorial(n) = n * (n - 1) * (n - 2) * ... 2 * 1
#####################################################################


print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("This program will calculate the factorial of a number")
print ("To quit the program, please enter 'quit' or 'q'!")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

while (True):
    inp = str(raw_input("Please enter a number -> "))

    # quit the program
    if inp == 'quit' or inp == 'q':
        print ("Goodbye...")
        break

    # handle the invalid input 
    if not inp.isdigit() or inp < 0:
        print ("Invalid input...")
        continue 

    # calculate the factorial
    # factorial(n) = n * (n - 1) * (n - 2) * ... 2 * 1
    num = int(inp)
    factorial = 1
    for i in range(num, 1, -1):
        factorial = factorial * i
    print ("factorial is "+ str(factorial))
        
    
 
