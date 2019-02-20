#!/usr/bin/env python


## Mihir Patel
## 2/20/19
## A program which will find all numbers that are divisible by
## 7 and not a multiple of 5, between 2000 and 3200 (both included)
## File : div_by_7_and_not_mult_of_5.py

##################################################################
def main():
##################################################################
    MIN = 2000
    MAX = 3200
    numbers = []
    for i in range (MIN, MAX + 1):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)

    print("There are " + str(len(numbers)) + " such numbers" )
    print("Below is a list of them")
    print(numbers)
    
# main()
    
if __name__ == "__main__":
    main()
