
#!/usr/bin/env python

###################################################################
# Author : Mihir Patel
#   Date : May 4, 2017
#   Desc : convert between temperature units.
###################################################################

print ("------------------------------------------------------")
print ("This program will convert between temperature units!")
print ("Input 'c'/'f' as a suffix for celsius/fahrenheit...")
print ("Ex: 100c to refer to 100 celsius..")
print ("Enter 'quit' or 'q' to exit the program!")
print ("------------------------------------------------------")

while (True):
    inp = input("Enter a value to convert : ")
    
    # allow to quit
    if inp == 'quit' or inp == 'q':
        print ("\n\n")
        print ("Goodbye....")
        break

    # perform the conversion and display the result
    val = float(inp[0:-1])
    if (inp[-1] != 'c' and  inp[-1] != 'f') or (not isinstance(val, float)):
        print ("Incorrect format...")
        continue
    else:
        if inp[-1] == 'c':
            print (str(val) + " celsius is ", str(((9/5) * val) + 32) + " fahrenheit ") 
        else:
            print (str(val) + " fahrenheit is ", str((val - 32) * (5 / 9)) + " celsius ") 


