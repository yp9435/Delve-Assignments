"""Question
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
"""

#Answer
x, y = map(int, input("Enter rows,columns:").split(","))
#x,y=3,5
matrix=[]
for i in range(x):
    temp=[]
    for j in range(y):
        temp.append(i*j)
    matrix.append(temp)
print(matrix)