#Using For Loop
row=int(input("Enter The Size Of Rows"))
for a in range(row):
    for c in range(a):
        print("*",end="")
    for space in range(row-a):
        print("  ",end="")
    for c in range(a):
        print("*",end="")
    print()
i=0
for b in reversed(range(row)):
    for num in (range(b)):
         print("*",end="")
    for space in range(i+1):
        print(" ",end="")
    i+=1
    for space2 in range(i):
        print(" ",end="")
    for a in range(b):
        print("*",end="")
    print()

print()
#Using While Loop
a=0
while(a<row):
    c=0
    while(c<a):
        print("*",end="")
        c+=1
    space=0
    while(space<row-a):
        print("  ",end="")
        space+=1
    c=0
    while(c<a):
        print("*",end="")
        c+=1
    print()
    a+=1
i=0
b=row
while(b>0):
    num=0
    while(num<b-1):
        print("*",end="")
        num+=1
    space=0
    while(space<i+2):
        print(" ",end="")
        space+=1
    i+=1
    space2=0
    while(space2<i-1):
        print(" ",end="")
        space2+=1
    a=0
    while(a<b-1):
        print("*",end="")
        a+=1
    b-=1
    print()