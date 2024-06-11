"""Question
Find the minimum possible denominations for given valid currency.
(No of currencies used should be minimum)
Expected Input 1:
valid_currency: [1,2,5,10,20,50,100,200,500,2000]
Money: 210
Expected Output:
200-1
10-1
Expected Input 2:
valid_currency: [1,2,5,10,20,50,100,200,500]
Money: 556
Expected Output:
500-1
50-1
5-1
1-1
"""

"""result = []
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
"""
#Answer
valid_currency = eval(input("Enter a list of valid currency: "))
amount= int(input("Money:"))
#valid_currency= [1,2,5,10,20,50,100,200,500,2000]
#amount= 556

valid_currency.sort(reverse=True)
#print(valid_currency)
result={}
count=0
for i in valid_currency:
    if amount >= i:
        count = amount // i
        amount -= i * count
        result[i] = count

for i in result:
    print(i,'-',result[i])


