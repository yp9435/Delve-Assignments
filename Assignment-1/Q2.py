"""Question
Write a program that accepts a comma separated sequence of words as input and prints the words in a 
comma-separated sequence after sorting them alphabetically."""

#Answer
string=input("Enter words seperated by commas:")
#string="without,hello,bag,world"

words= string.split(',')
sort_words= sorted(words)
res=','.join(sort_words)
print("Result:",res)
