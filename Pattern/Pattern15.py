#Using For Loop
row=int(input("Enter The Number Of Rows "))
for i in range(row):
    for  space in range(i):
        print(" ",end="")
    print("*",end="")
    for spaceinnner in range(row-i):
        print(" ",end=" ")
    print("*")
for j in range(row):
    for space in range(row-j):
        print(" ",end="")
    print("*",end="")
    for spaceinner in range(j):
        print(" ",end=" ")
    print("*")
 
print()

#Using While Loop
r=0
while(r<row):
    space=0
    while(space<r):
        print(" ",end="")
        space+=1
    print("*",end="")
    spaceinner=0
    while(spaceinner<row-r):
        print(" ",end=" ")
        spaceinner+=1
    print("*")
    r+=1

s=0
while(s<row):
    space=0
    while(space<row-s):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<s):
        print(" ",end=" ")
        innerspace+=1
    print("*")
    s+=1


