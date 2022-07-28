row=int(input("Enter The Number Of Rows"))
j=row
for i in range(row):
    for space in range(i):
        print(" ",end="")
    for a in range(j):
        print("* ",end="")
    j=j-1
    print()
#Using While Loop
k=row
m=0
while(m<=row):
    spaces=0
    while(spaces<=m):
        print(" ",end="")
        spaces=spaces+1
    n=0
    while(n<=k-1):
        print("* ",end="")
        n=n+1
    k=k-1
    m=m+1
    print()