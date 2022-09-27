import time as t
#Pattern2
#Using For Loop
row=int(input("Enter The Number Of Rows"))
j=row
for i in range(row):
    for space in range(i):
        print(" ",end=" ")
    for a in range(j):
        print("* ",end="")
    t.sleep(0.25)
    j=j-1
    print()

print()
#Using While Loop
k=row
m=0
while(m<=row):
    spaces=1
    while(spaces<=m):
        print(" ",end=" ")
        spaces=spaces+1
    n=1
    while(n<=k):
        print("* ",end="")
        n=n+1
    t.sleep(0.25)
    k=k-1
    m=m+1
    print()