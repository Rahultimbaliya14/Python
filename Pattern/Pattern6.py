import  time as t
#Using For Loop
row=int(input("Enter The Size Of The Row"))
n=row
for n in reversed(range(row+1)):
    for a in range(n):
        print("* ",end="")
    t.sleep(0.20)
    print()
for row in range(row+1):
    for a in range(row):
        print("* ",end="")
    t.sleep(0.20)
    print()

print()    
#Using While Loop


m=0
while(m<row):
    p=m
    while(p<row):
        print("* ",end="")
        p=p+1
    t.sleep(0.20)
    m=m+1
    print()
print()
q=0
while(q<=row):
    r=q
    while(r>0):
        print("* ",end="")
        r-=1
    t.sleep(0.20)
    q+=1
    print()