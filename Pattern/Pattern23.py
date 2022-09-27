#Usign For Loop
row=int(input("Enter The Number Of Rows "))
for i in range(row):
    i2=i+i
    for space in range(row*2-i2):
        print(" ",end="")
    for m in range(i):
        print("*",end="")
    print()
h=2
for i in reversed(range(row)):
    i2=i+h
    for space in range(row-i2):
        print(" ",end="")
    print(" ",end="")
    for a in range(i):
        print("*",end="")
    print()
    h+=1

#Using While Loop
i=0
while(i<row):
    i2=i+i
    space=0
    while(space<row*2-i2):
        print(" ",end="")
        space+=1
    m=0
    while(m<i):
        print("*",end="")
        m+=1
    print()
    i+=1
i=row
h=1
while(i>0):
    i2=i+h
    space=0
    while(space<row-i2):
        print(" ",end="")
        space+=1
    a=0
    while(a<i):
        print("*",end="")
        a+=1
    print()
    i-=1
    h+=1