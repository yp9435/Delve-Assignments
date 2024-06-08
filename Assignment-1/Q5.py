"""Question
Write a program that accepts a sentence and calculate the number of letters 
and digits.
"""

#Answer
string=input("Enter a sentence:")
#string="hello world! 123"
letters,digits=0,0
for i in string:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
    else:
        pass

print("LETTERS ",letters)
print("DIGITS ",digits)