"""Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The numbers after the direction are steps.  
The trace of robot movement is shown as the following:
Expected Input:
UP 5
DOWN 3
LEFT 3
RIGHT 2
"""

#Answer
x,y=0,0
intialpos=(0,0)
finalpos=(x,y)
while True:
    movement=input("Enter direction, steps:")
    if not movement:
        break
    direction, steps=movement.split()
    steps=int(steps)

    if direction == "UP":
        y+=steps
    elif direction == "DOWN":
        y-=steps
    elif direction == "RIGHT":
        x+=steps
    elif direction == "LEFT":
        x-=steps
finalpos=(x,y)
print("The Intial Position of the robot is",intialpos,"and the Final Position is",finalpos)



