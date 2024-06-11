"""Question
A gaming company wants to create an App with multiple games. 
The instruction of the games is given. You are asked to write the code to prepare the games,
Where inputs will be taken from users. Once the gaming algorithm is prepared then it can be associated with production interface of the App.

Game: Stone Paper Scissor Cut
    
Each win of a player will be counted as a one point for the player. 
The game continues until any of the player scores 5.

Expected Input:       Expected Output:
Player A   Player B    		Result
Stone       Stone      		DRAW
Stone       Paper   		Player B wins
Stone       Scissor 		Player A wins
Paper       Stone   		Player A wins
Paper       Paper   		DRAW
Paper       Scissor 		Player B wins
Scissor     Scissor 		DRAW
Scissor     Stone   		Player B wins
Scissor     Paper   		Player A wins
"""

#Answer
scorea,scoreb=0,0
table=[['A','B','Result']]
while scorea <5 and scoreb <5:
    a,b=map(str,input("Enter Player A, PLayer B moves:").split(','))
    allmovesdict={('stone', 'paper'): 'Player B wins',('stone', 'scissor'): 'Player A wins',('paper', 'stone'): 'Player A wins',('paper', 'scissor'): 'Player B wins',('scissor', 'stone'): 'Player B wins',('scissor', 'paper'): 'Player A wins'}
    if a==b:
        print("DRAW")
        move='DRAW'
    else:
        move=allmovesdict[(a,b)]
        print(move)
        if move == "Player A wins":
            scorea+=1
        else:
            scoreb+=1
    #print("A:",scorea,"B:",scoreb)
    table.append([a,b,move])
print('-'*12)

print("\n\nTABLE")
for i in table:
    print(i[0],'\t',i[1],'\t',i[2])

print("Final Score A:",scorea,"B:",scoreb)
if scorea==5:
    print("Player A wins Overall!!!")
elif scoreb==5:
    print("Player B wins Overall!!!")