#Using For Loop
row=int(input("Enter The Number Of Rows: "))
for i in range(row):
    for space in range(row-i):
        print(" ",end="")
    if(i==0 or i==row-1 or i==int(row/2) ):
        for a in range(row+2):
            print("*",end="")
        print()
    else:
        print("*",end="")
        for innerspace in range(row):
            print(" ",end="")
        print("*",end="")
        print()

print()

#Using While Loop
i=0
while(i<row):
    space=0
    while(space<row-i):
        print(" ",end="")
        space+=1
    if(i==0 or i==row-1 or i==int(row/2) ):
        a=0
        while(a<row+2):
            print("*",end="")
            a+=1
        print()
    else:
        print("*",end="")
        innerspace=0
        while(innerspace<row):
            print(" ",end="")
            innerspace+=1
        print("*",end="")
        print()
    i+=1