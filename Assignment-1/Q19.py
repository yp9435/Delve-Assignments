"""Question
Cyclic rotation: 

Case 1: first element moves to last and rest all the elements move one step to left  
Case 2: last element moves to first and rest all the element move  one step to right 

Input 1 Description: 1 - first to last  2- last to first
Input 2 Description : string
Input 3 Description : no of times
Expected Input 1:
1
'happy'
2
Expected Output:
Appyh
ppyha

"""

#Answer
case=int(input("Enter Case 1/Case 2:"))
string=input("Enter the string:")
n=int(input('Enter the no of times:'))

if case==1:
    for i in range(n):
        string=string[1:]+string[0]
        print(string)
if case==2:
    for i in range(n):
        string=string[-1]+string[:-1]
        print(string)
