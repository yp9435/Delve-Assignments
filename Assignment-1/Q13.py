"""Question
Find how many pairs in a binary number that starts and ends with 1
Expected Input 1:
100101
Expected Output:
2
Expected Input 2:
1001101010010
Expected Output:
15
"""

#Answer
binarynum = input("Enter a Binary number:")

posof1=[i for i in range(len(binarynum)) if binarynum[i]=='1']
count=0

for i in range(len(posof1)): #start
    for j in range(i+1,len(posof1)): #end
        count+=1

print(count)

