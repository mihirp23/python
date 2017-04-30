#!/usr/bin/env python

###################################################################
# Author : Mihir Patel
#   Date : April 30, 2017
#   Desc : display the first 100 prime numbers.
###################################################################

###################################################################
def is_prime(n):
###################################################################
# Purpose of this function is to determine whether the provided
# number is a prime number, that is, it is only divisible by
# 1 and itself.

    # base case
    if n == 1 or n == 2:
        return True
    
    # start at 3 and go through all odd numbers since 2 
    # is the only even prime number    
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    
    return True
# is_prime()
    

###################################################################
if __name__ == "__main__":
###################################################################
# generate and display first 100 prime numbers.

    counter = 0
    n = 1
    while (counter < 100):
        if is_prime(n):
            print (n)
            counter += 1
        n += 1
# main()
    
