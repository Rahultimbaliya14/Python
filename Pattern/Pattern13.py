from pickle import EMPTY_DICT

#Using The For Loop
row=int(input("Enter The Size Of Rows "))
for i in range(row+1):
    for space in range(row-i):
        print(" ",end="")
    print("*" ,end="")
    for spaceinnner in range(i+i):
        print(" ",end="")
    print("*",end="")
    print()
for s in range(row+2):
    print("* ",end="")

print()
#Using While Loop

k=0
while(k<=row):
    space1=0
    while(space1<=row-k):
        print(" ",end="")
        space1+=1
    print("*",end="")
    spaceinner=0
    while(spaceinner<=k+k):
        print(" ",end="")
        spaceinner+=1
    print("*",end="")
    print()
    k+=1
a=0
while (a<=row+2):
    print("* ",end="")
    a+=1    