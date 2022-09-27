#Using For Loop
row=int(input("Enter The Only Even Number Of Rows  "))
for i in range(row):
    for space in range(row-i):
        print(" ",end="")
    for a in range(i):
        print("*",end=" ")
    print()
for j in range(int(row/3)):
    for a in range(int(row/3)):
        print(" *",end="")
    for space in range(int(row-row/3)):
        print(" ",end="")
    for b in range(int(row/3)):
        print(" *",end="")
    print()
 
#Using While Loop
i=0
while(i<row):
    space=0
    while(space<row-i):
        print(" ",end="")
        space+=1
    a=0
    while(a<i):
        print("*",end=" ")
        a+=1
    i+=1
    print()
j=0
while(j<int(row/3)):
    a=0
    while(a<int(row/3)):
        print(" *",end="")
        a+=1
    space=0
    while(space<int(row-row/3)):
        print(" ",end="")
        space+=1
    b=0
    while(b<int(row/3)):
        print(" *",end="")
        b+=1
    j+=1
    print()