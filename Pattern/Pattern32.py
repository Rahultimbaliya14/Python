#Using For Loop
row=int(input("Enter The Number Of Rows: "))
for i in range(int(row/2)):
    for space in range(int(row/2-i)):
        print(" ",end="")
    print('*',end="")
    for space in range(i):
        print(" ",end="")
    print("*",end="")
    print()
for i in range(int(row/2)):
    for space in range(i):
        print(" ",end="")
    print("*",end="")
    for space in range(int(row/2-i)):
        print(" ",end="")
    print("*",end="")
    print()


print()

#Using While Loop
i=0
while(i<int(row/2)):
    space=0
    while(space<int(row/2-i)):
        print(" ",end="")
        space+=1
    print("*",end="")
    space=0
    while(space<i):
        print(" ",end="")
        space+=1
    print("*",end="")
    i+=1
    print()
i=0
while(i<int(row/2)):
    space=0
    while(space<i):
        print(" ",end="")
        space+=1
    print("*",end="")
    space=0
    while(space<int(row/2-i)):
        print(" ",end="")
        space+=1
    print("*",end="")
    i+=1
    print()
