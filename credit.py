#!/usr/bin/env python

###################################################################
# Author : Mihir Patel
#   Date : April 30, 2017
#   Desc : validate the credit card number using Luhn's algorithm.
###################################################################


###################################################################
def is_valid_credit_card(inp):
###################################################################
# validate the credit card number that is provided using Luhn's 
# algorithm, which is as follows : 
# 1. Drop the last digit from the number and keep that for later.
# 2. Reverse the digits
# 3. Double the digits that are in odd position (1st, 3rd, etc..)
# 4. Subtract 9 from digits that greater than 9.
# 5. Sum all the digits and then divide the sum by 10.
#    The resulting remainder then should be the same as the number
#    from step #1 (check digit).

    # invalid input...
    if not inp.isdigit():
        return False
    else:
        cc_num = [int(i) for i in inp]

        # step 1
        last_digit = cc_num.pop()
        
        # step 2
        cc_num.reverse()

        # step 3 : multiply odd digits by 2
        for i in range(0, len(cc_num)):
            if (i + 1) % 2 != 0:
                cc_num[i] *= 2 

        # step 4 : subtract 9 from digits greater than 9
        for i in range(0, len(cc_num)):
            if cc_num[i] > 9:
                cc_num[i] -= 9
        
        # step 5 : check digit
        sm = sum(cc_num)
        if sm % 10 == last_digit:
            return True
   
    # at this point, the input is invalid... 
    return False    
# is_valid_credit_card()

###################################################################
if __name__ == "__main__":
###################################################################
    print ("++++++++++++++++++++++++++++++++++++++++")
    print ("Welcome to the Credit Card Validator!")
    print ("Enter 'quit' or 'q' to quit the program.")
    print ("++++++++++++++++++++++++++++++++++++++++")
    print
    while (True):
        credit_input = raw_input("Please enter number -> ")

        if credit_input == "quit" or credit_input == "q":
            break

        if not is_valid_credit_card(credit_input):
            print ("Credit Card is INVALID!!!")
        else:
            print ("VALID")
# main()
    



