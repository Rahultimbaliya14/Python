#using For Lopp
from audioop import reverse
from pkg_resources import ensure_directory
row=int(input("Enter The Size Of Rows"))
for a in range(row):
    for c in range(a):
        print("*",end="")
    print()
for b in reversed(range(row+1)):
    for num in (range(b)):
         print("*",end="")
    print()

#Using While Loop
j=0
while(j<=row):
    k=1
    while(k<j):
        print("*",end="")
        k+=1
    print()
    j+=1
p=row
while(p>0):
    n=p
    while(n>0):
        print("*",end="")
        n-=1
    print()
    p-=1