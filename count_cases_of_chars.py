#!/usr/bin/env python

## Mihir Patel
## 2/19/19
## A program that accepts a sentence and calculate the number of
## upper case letters and lower case letters. 

##################################################################
def main():
##################################################################
   print("I will count the number of uppercase and lowercase")
   print("letters typed by you!")

   inp_str = input("please type your input -> ")

   upper_count = 0
   lower_count = 0
   for c in inp_str:
        if c.isupper():
           upper_count +=1
        elif c.islower():
           lower_count +=1
        

   print("Number of uppercase letters: " + str(upper_count))
   print("Number of lowercase letters: " + str(lower_count))
    
# main()

if __name__ == "__main__":
    main()
