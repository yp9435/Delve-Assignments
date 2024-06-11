"""Question
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Passwords that match the criteria are to be printed, each separated by a comma.
"""

#Answer
passwords = input("Enter the passwords:").split(",")
#passwords = "ABd1234@1,a F1#,2w3E*,2We3345"
valid = []
hasalength = False
for i in passwords:
    if len(i) >= 6 and len(i) <= 12:
        hasalength = True
    hasalower = any(c.islower() for c in i)
    hasaupper = any(c.isupper() for c in i)
    hasadigit = any(c.isdigit() for c in i)
    hasaspecial = any(c in '$#@' for c in i)
    hasaspace = any(c == ' ' for c in i)

    #print(i," - ",hasalength,hasaupper,hasalower,hasadigit,hasaspecial,hasaspace)
    if hasadigit and hasalength and hasalower and hasaupper and hasaspecial and (hasaspace == False):
        valid.append(i)

#print(valid)
print("Valid passwords:", ','.join(valid))


