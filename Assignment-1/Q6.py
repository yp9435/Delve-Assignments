"""Question
Write a program that accepts a sentence and calculate the number of upper case 
letters and lower case letters.
"""

#Answer
string=input("Enter a sentence:")
#string="Hello world!"

upperc,lowerc=0,0
for i in string:
    if i.isupper():
        upperc+=1
    elif i.islower():
        lowerc+=1
    else:
        pass

print("UPPER CASE ",upperc,"\nLOWER CASE ",lowerc)