"""Question
There is a bus travelling from Town A to Town B. There are n stops between them and bus has to make m stops.
Find the numbery of ways in the travel so that no stop is consecutive
Expected Input 1:
n=12
m=4
Expected Output:
Output :126
Expected Input 2:
n = 16
s = 5
Expected Output:
792
"""

#Answer
from math import comb
n, m = map(int, input("Enter total number of stops(n) and number of stops the bus makes(m):").split(","))

if m>n:
    pass
else:
    result=comb(n - m + 1, m)#combination formula
print("The number of ways in the travel between Town A and Town B so that no stop is consecutive:",result)
