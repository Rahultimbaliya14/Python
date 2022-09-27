#Using For Loop
row=int(input("Enter The Number Of Rows "))
i=row
for i in reversed(range(row)):
    for space in range(i):
        print(" ",end=" ")
    for a in range(row-i):
        print("*",end=" ")
    for space1 in range(i):
        print(" ",end="")
    for a1 in range(row-i):
        print("*",end=" ")
    for space2 in range(i):
        print(" ",end="")
    for a3 in range(row-i):
        print("*",end=" ")
    print()


#Using While Loop

j=row
while(j>0):
    spaces=0
    while(spaces<j):
        print(" ",end=" ")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    spaces=0
    while(spaces<j):
        print(" ",end="")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    spaces=0
    while(spaces<j):
        print(" ",end="")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    print()
    j-=1