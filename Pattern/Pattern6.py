row=int(input("Enter The Size Of The Row"))
n=row
for n in reversed(range(row+1)):
    for a in range(n):
        print("* ",end="")
    print()
for row in range(row+1):
    for a in range(row):
        print("* ",end="")
    print()

print()    
#Using While Loop


m=0
while(m<row):
    p=m
    while(p<row):
        print("* ",end="")
        p=p+1
    m=m+1
    print()
print()
q=0
while(q<=row):
    r=q
    while(r>0):
        print("* ",end="")
        r-=1
    q+=1
    print()