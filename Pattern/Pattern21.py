#Using For Loop
row=int(input("Enter The Number Of Rows "))
for i in range(row):
    row2=row+row
    for space in range(row2-i):
        print(" ",end="")
    for a in range(i):
        print("*",end=" ")
    print()
for j in range(row):
    for space in range(row-j):
        print(" ",end="")
    for b in range(j):
        print("*",end="")
    for spaceinner in range(row*2):
        print(" ",end="")
    for d in range(j):
        print("*",end="")
    print()
h=0
for k in reversed(range(row)):
    for space in range(h+1):
        print(" ",end="")
    h+=1
    for j in range(k):
        print("*",end="")
    for spaceinner in range(row*2):
        print(" ",end="")
    for l in range(k):
        print("*",end="")
    print()
for c in reversed(range(row)):
    for space in range(row2-c):
        print(" ",end="")
    for a in range(c):
        print("*",end=" ")
    print()

#Using While Loop
i=0
while(i<row):
   row2=row+row
   space=0
   while(space<row2-i):
       print(" ",end="")
       space+=1
   a=0
   while(a<i):
       print("*",end=" ")
       a+=1
   print()
   i+=1 
j=0
while(j<row):
    space=0
    while(space<row-j):
        print(" ",end="")
        space+=1
    b=0
    while(b<j):
        print("*",end="")
        b+=1
    spaceinner=0
    while(spaceinner<row*2):
        print(" ",end="")
        spaceinner+=1
    d=0
    while(d<j):
        print("*",end="")
        d+=1
    j+=1
    print()
k=row
h=0
while(k>0):
    space=0
    while(space<h):
        print(" ",end="")
        space+=1
    h+=1
    j=k
    while(j>0):
        print("*",end="")
        j-=1
    spaceinner=0
    while(spaceinner<row*2):
        print(" ",end="")
        spaceinner+=1
    l=k
    while(l>0):
        print("*",end="")
        l-=1
    k-=1
    print()
print()
c=row-1
while(c>0):
    space=0
    while(space<row2-c):
        print(" ",end="")
        space+=1
    a=0
    while(a<c):
        print("*",end=" ")
        a+=1
    c-=1
    print()
