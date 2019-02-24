#!/usr/bin/env python3

## Mihir Patel
## 2/24/19
## Program that takes a number from user 
## and displays if it's even or odd
## File : even_or_odd.py


############################################################
def main():
############################################################

    # ask user
    while (True):
         try:
             num = int(input("Enter a number: "))
             break
         except:
             # handle invalid entries by user
             print("Invalid input, please try again...")

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

# main()

if __name__ == "__main__":
    main()
