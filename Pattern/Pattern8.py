import time as t
#Using For Loop
row=int(input("Enter The Number Of Rows"))
for row in range(row+1):
    for a in range(row):
        print("* ",end="")
    t.sleep(0.20)
    print()
j=row
for i in range(row):
    for space in range(i):
        print(" ",end=" ")
    for a in range(j):
        print("* ",end="")
    t.sleep(0.20)
    j=j-1
    print()


#Using While Loop
q=0
while(q<=row):
    r=q
    while(r>0):
        print("* ",end="")
        r-=1
    t.sleep(0.20)
    q+=1
    print()
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
    t.sleep(0.20)
    k=k-1
    m=m+1
    print()