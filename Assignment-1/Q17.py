"""Question
Validate Email Address:
     a. Check for '@' symbol, it should be only 1
     b. Only lower-case letters are allowed
     c. Numbers are allowed
     e. No symbols allowed other than '.' & '_'

"""

#Answer
email=input('Enter E-mail Adress:')
lowercase=email.islower()
if (email.count('@'))==1:
    atsymbol=True
else:
    atsymbol=False
special=True
for i in '!#$%^&*():<>?~|+=-,':
    if i in email:
        special=False

if lowercase and atsymbol and special:
    print("Valid Email ID!")
else:
    print('Invalid!')