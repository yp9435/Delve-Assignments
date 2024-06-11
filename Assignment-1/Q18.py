"""Question
Solve the following patterns 

Input Description:   row count

Expected Input:
 4
Expected Output:

1
2 * 3
4 * 5 * 6
7 * 8 * 9 * 10

Input Description:   row count

Expected Input:
4
Expected Output:

      *
    *  *
   * * *
  * * * *
   * * *
    *  *
      *

Input Description:   row count

Expected Input:
4

Expected Output:

1
2 * 3
4 * 5 * 6
7 * 8 * 9 * 10
4 * 5 * 6
2 * 3
1

Program to print the pattern ‘G’
Input Description : No of rows

Expected Input:
7
Expected Output:

  ***  
 *     
 *     
 * *** 
 *      * 
 *      * 
  * * *  


Input Description:   row count (only odd)
Expected Input:
5
Expected Output:

1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
1 1 1 1 1

"""

#Answer
def optiona(row):
    count=1
    for i in range(1,row+1):
        for j in range(i):
            if j>0:
                print('*',end='')
            print(count,end='')
            count+=1
        print()

def optionb(row):
    for i in range(row):
        for j in range(row - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    
    for i in range(row - 2, -1, -1):
        for j in range(row - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

def optionc(row):
    count = 1
    for i in range(1, row + 1):
        for j in range(i):
            if j > 0:
                print(" * ", end="")
            print(count, end="")
            count += 1
        print()

    start = count - (row - 1)
    
    for i in range(row - 1, 0, -1):
        count = start
        for j in range(i):
            if j > 0:
                print(" * ", end="")
            print(count, end="")
            count += 1
        start -= (i - 1)
        print()  

def optiond(row):
    for i in range(row):
        if i == 0:
            print(" ***  ")
        elif i < row - 3:
            print("*      ")
        elif i == row - 3:
            print("*  *** ")
        elif i == row - 2:
            print("*     *")
        elif i == row - 1:
            print(" * * * ")
        else:
            print("*     *")

def optione(row):
    for i in range(row):
        for j in range(row):
            if i == 0 or i == row - 1:
                print("1", end=" ")
            elif j == row // 2:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

loop=True
while loop:
    print("MENU\na - ascending * triangle\nb - diamond pattern\nc - ascending/descending * triangle\nd - G pattern\ne - odd number 010")
    choice = input("Enter your choice (a/b/c/d/e): ").lower()
    if choice == 'a':
        row=int(input('Enter the number of rows:'))
        optiona(row)
    elif choice == 'b':
        row=int(input('Enter the number of rows:'))
        optionb(row)
    elif choice == 'c':
        row=int(input('Enter the number of rows:'))
        optionc(row)
    elif choice == 'd':
        optiond(7)
    elif choice == 'e':
        row=int(input('Enter odd number of rows:'))
        optione(row)
    else:
        loop=False
        break