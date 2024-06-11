"""Question
You are required to write a program to sort the (name, age, height) tuples 
by ascending order where name is string, age and height are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
"""

#Answer
tupledata=[]
while True:
    temp = input("Enter name,age,height:")
    if not temp:
        break
    name,age,height= temp.split(',')
    tupledata.append((name,int(age),int(height)))
result=sorted(tupledata, key=lambda x: (x[0],x[1],x[2]))
print(result)
