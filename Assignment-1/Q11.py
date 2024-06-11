"""Question
Find the continuous occurrence of the string.
Expected Input:
Aabbcdeefffaabbcc
Expected Output:
a2b2c1d1e2f3a2b2c2
"""

#Answer
#string = "Aabbcdeefffaabbcc"
string = input("Enter a string:").lower()

result = []
count = 1
currentch = string[0]

for i in range(1,len(string)):
    if string[i] == currentch:
        count+=1
    else:
        result.append(currentch+str(count))
        currentch = string[i]
        count=1
result.append(currentch+str(count))
#print(result)
print(''.join(result))




    


