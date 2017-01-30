'''
.SYNOPSIS
    incrementing a user input integer
.DESCRIPTION
    It will take input from the user. converts it into the data type float and the number will be rounded off.
    If the user has entered 1.2 then it will convert that into 1, if 1.7 then it will be 2. 
.NOTES
    File Name      : IncrementInteger.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Copyright      - none
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
a = input("type a number to increment: ")
print("The below input will be used to match against the incremented number. The incrementation of the number will stop if it is not less than the number that you are entering below")
b = input("The top limit of the incemented number?: ")
b = round(float(b))
a = round(float(a))
while a < b:
    a += 1
    print (a)