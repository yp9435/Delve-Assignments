"""Question
Convert Decimal to binary (Without inbuilt function)
Expected Input 1:
12
Expected Output:
1100
Expected Input 2:
20
Expected Output :
10100
"""

#Answer
num=int(input('Enter a decimal number:'))
if num == 0:
    print("Result: 0")
else:
    binary = ""
    while num > 0:
        rem = num % 2  
        binary = str(rem) + binary  
        num //= 2 
    print("Result:",binary)