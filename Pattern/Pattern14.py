#Using The For Loop
row=int(input("Enter The Number oof The Rows "))
for i in range(row):
    for space in range(row-i):
        print(" ",end=" ")
    for a in range(i):
        print(i,end="   ")
    print()

#using While Loop
j=0
while(j<row):
    space=0
    while(space<row-j):
        print(" ",end=" ")
        space+=1
    k=0
    while(k<j):
        print(j,end="   ")
        k+=1
    j+=1
    print()