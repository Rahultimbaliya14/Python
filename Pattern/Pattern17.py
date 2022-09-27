#Using For Loop
row=int(input("Enter The Numner Of Rows "))
for i in range(row):
    for m in range(row):
        for a in range(i):
            print("  ",end="")
        for j in range(row-i):
            print("*",end=" ")
    print()


print()

#Using While Loop
k=0
while(k<row):
    g=0
    while(g<row):
        h=0
        while(h<k):
            print("  ",end="")
            h+=1
        l=0
        while(l<row-k):
            print("*",end=" ")
            l+=1
        g+=1
    k+=1
    print()