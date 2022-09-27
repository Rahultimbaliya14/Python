#Using For Loop
row=int(input("Enter The Number Of Rows: "))
for i in range(int(row/2)):
    print("*",end="")
    if(i==0 or i==int(row/2-1)):
        for space in range(int(row/2)):
               print("* ",end="")
    else:
        for space in range(int(row/2)):
               print(" ",end=" ")
        print("*",end="")
    print()
for j in range(int(row/2)):
    print("*",end="")
    for space in range(j+1):
        print(" ",end=" ")
    print("*",end="")
    print()


print()


#Using While Loop
i=0
while(i<int(row/2)):
    print("*",end="")
    if(i==0 or i==int(row/2-1)):
        space=0
        while(space<int(row/2)):
            print("* ",end="")
            space+=1
    else:
        space=0
        while(space<int(row/2)):
            print(" ",end=" ")
            space+=1
        print("*",end="")
    i+=1
    print()
j=0
while(j<int(row/2)):
    print("*",end="")
    space=0
    while(space<j+1):
        print(" ",end=" ")
        space+=1
    print("*",end="")
    j+=1
    print()
    

