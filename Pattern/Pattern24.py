#Using For Loop
row=int(input("Enter The Number Of Rows "))
for sapce2 in range(row*3+4):
        print("* ",end="")
print()
for i in range(row):
    print("*",end="")
    for space in range(row*3-i):
        print(" ",end="")
    print("*",end="")
    for innerspace in range(i):
        print(" ",end=" ")
    print("* ",end="")
    for space in range(row*3-i+2):
        print(" ",end="")
    print("*",end="")
    print()
for sapce2 in range(row*3+4):
        print("* ",end="")

print()

#Using While Loop
space2=0
while(space2<row*3+4):
    print("* ",end="")
    space2+=1
print()
i=0
while(i<row):
    print("*",end="")
    space=0
    while(space<row*3-i):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<i):
        print(" ",end=" ")
        innerspace+=1
    print("* ",end="")
    space=0
    while(space<row*3-i+2):
        print(" ",end="")
        space+=1
    print("*",end="")
    print()
    i+=1
space2=0
while(space2<row*3+4):
    print("* ",end="")
    space2+=1