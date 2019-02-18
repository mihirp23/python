#!/usr/bin/env python

## Mihir Patel
## 2/18/19
## Calculate the area of a circle based on the radius
## provided by user.

import math # for value of pi
##################################################################
def main():
##################################################################
    print ("I will calculate radius of circle")

    # ask user to enter radius
    while (True):
        try:
            radius = float(input("Enter radius: "))
            break
        except:
            # invalid input was provided
            # so, keep asking user until a valid input is
            # provided
            print("invalid input, please try again...")

    area = math.pi * (radius * radius)    
    print ("radius of circle : " + str(area))
# main()

if __name__ == "__main__":
    main()
