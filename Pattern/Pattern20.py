#Using For Loop
row=int(input("Enter The Number Of Rows "))
j=0
for i in reversed(range(row+1)):
    for a in range(i):
        print("*",end="")
    for space1 in range(j):
        print(" ",end=" ")
    j+=1
    for a in range(i):
        print("*" ,end="")
    print()
for i in range(row+1):
    for a in range(i):
        print("*",end="")
    for space in range(row-i):
        print(" ",end=" ")
    for s in range(i):
        print("*",end="")
    print()    

print()
#Using While Loop
i=row
k=0
while(i>=0):
    j=0
    while(j<i):
        print("*",end="")
        j+=1
    l=0
    while(l<k):
        print(" ",end=" ")
        l+=1
    m=0
    while(m<i):
        print("*",end="")
        m+=1
    k+=1
    i-=1
    print()
a=0
while(a<=row):
    f=0
    while(f<a):
        print("*",end="")
        f+=1
    space=0
    while(space<row-a):
        print(" ",end=" ")
        space+=1
    s=0
    while(s<a):
        print("*",end="")
        s+=1
    a+=1
    print()
    