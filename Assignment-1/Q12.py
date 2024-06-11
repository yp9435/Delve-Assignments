"""Question
Find the pair of alphabets in an alphanumeric string whose sum of numbers in between is always 9
Expected Input 1:
a54b12c
Expected Output:
a,b
Expected Input 2:
a55b234cd9f63de54x3m
Expected Output:
b,c
b,d
d,f
f,d
f,e
e,x
"""

#Answer
string = input("Enter a string:")
pairs=[]
n=len(string)
i=0
while i<n:
    if string[i].isalpha():
        start=string[i]
        digit=[]
        i+=1
        while i<n and string[i].isdigit():
            digit.append(int(string[i]))
            i+=1
        if i<n and string[i].isalpha():
            end=string[i]
            print(sum(digit))
            if sum(digit)==9:
                pairs.append((start,end))
                if string[i+1].isalpha():
                    pairs.append((start,string[i+1]))
    else:
        i+=1
for i in pairs:
    print(','.join(i))