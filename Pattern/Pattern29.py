#Using For Loop
from re import L


row=int(input("Enter The Number Of Rows: "))
a=0
for i in reversed(range(row+2)):
    for space in range(a+1):
        print(" ",end="")
    a+=1
    for  b in range(row-a+2):
        print(b,end=" ")
    if(b==0):
        b=0
    else:
        print()
print()
for c in range(row+1):
    print(c,end=" ")
print()
for i in range(row+1):
    for space in range(row-i+1):
        print(" ",end="")
    for b in range(i+1):
        print(b,end=" ")
    print()
print()

#Using While Loop
a=0
i=row+2
while(i>1):
    space=0
    while(space<a+1):
        print(" ",end="")
        space+=1
    a+=1
    b=0
    while(b<row-a+2):
        print(b,end=" ")
        b+=1
    if(b==0):
        b=0
    else:
        print()
    i-=1
c=0
while(c<row+1):
    print(c,end=" ")
    c+=1
i=0
while(i<row+1):
    space=0
    while(space<row-i+2):
        print(" ",end="")
        space+=1
    b=0
    while(b<i):
        print(b,end=" ")
        b+=1
    i+=1
    print()
