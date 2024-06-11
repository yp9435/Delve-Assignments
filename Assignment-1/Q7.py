"""Question
Write a program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown 
as following:
D 100
W 200
D means deposit while W means withdrawal.
"""

#Answer
total=0
#D 300 D 300 W 200 D 100

while True:
    transaction = input("Enter transaction:")
    if not transaction:
        break
    action, samount = map(str, transaction.split(" "))
    amount = int(samount)
    if action == "D":
        total += amount
    elif action == "W":
        total -= amount

print("Total Amount:", total)

