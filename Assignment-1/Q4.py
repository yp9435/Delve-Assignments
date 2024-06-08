"""Question
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

#Answer
list_of_num=[]
start, end = map(int, input("Enter the limits:").split(","))
for i in range(start,end+1):
    if i%2==0:
        list_of_num.append(str(i))
res=",".join(list_of_num)
print("Even numbers in the range",start,"to",end,":",res)
