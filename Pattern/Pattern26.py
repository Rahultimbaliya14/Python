#Using For Loop
row=int(input("Enter The Number Of Rows: "))
for i in range(row):
    for space in range(row*3-i):
        print(" ",end="")
    print("*",end="")
    for innersace in range(i):
        print(" ",end=" ")
    print("*",end="")
    print()
for a in range(row*2):
    print("*",end="")
for space in range(row*2+2):
    print(" ",end="")
for a in range(row*2):
    print("*",end="")

print()
for i in range(row):
    for space in range(i):
        print(" ",end="") 
    print("*",end="")
    for space in range(row*6-i-i):
        print("*",end="")
    print("*",end="")
    print()


print()


#Using While Loop
i=0
while(i<row):
    space=0
    while(space<row*3-i):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<i):
        print(" ",end=" ")
        innerspace+=1
    print("*",end="")
    i+=1
    print()
a=0
while(a<row*2):
    print("*",end="")
    a+=1
space=0
while(space<row*2+2):
    print(" ",end="")
    space+=1
a=0
while(a<row*2):
    print("*",end="")
    a+=1
print()
i=0
while(i<row):
    space=0
    while(space<i):
        print(" ",end="")
        space+=1
    print("*",end="")
    space=0
    while(space<row*6-i-i):
        print("*",end="")
        space+=1
    print("*",end="")
    i+=1
    print()
    