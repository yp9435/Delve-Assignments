"""Question
Write a program that accepts a sequence of whitespace separated words as input and prints the words 
after removing all duplicate words and sorting them alphanumerically."""

#Answer
string=input("Enter the sentence:")
#string="hello world and practice makes perfect and hello world again"
uniquewords=set(string.split())
res=" ".join(sorted(uniquewords))
print("Result:",res)