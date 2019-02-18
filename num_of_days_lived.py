#!/usr/bin/env python

## Mihir Patel
## 2/18/19
## Calculate the number of days since user's birthday


import datetime # for date calculations

##################################################################
def main():
##################################################################
    print ("I will calculate the number of days since your birth")

    # ask user to enter radius
    while (True):
        try:
            year = int(input("enter year: "))
            month = int(input("enter month: "))
            day = int(input("enter day: "))
            birthday = datetime.date(year, month, day)
            break
        except:
            # invalid input was provided
            # so, keep asking user until a valid input is
            # provided
            print("You did not provide a valid input")

    current_date = datetime.date.today()
    time_delta = current_date - birthday
    print("Number of Days since your birth: " + str(time_delta.days))
    
# main()

if __name__ == "__main__":
    main()
