import time as t
#using for lopp
row=int(input("Enter The Size Of Rows "))
for i in range(row):
    for a in range(i+1):
        print("*",end="")
    t.sleep(0.20)
    row2=row-i
    for space in range(row2-i+row):
        print(" ",end="")
    for b in range(i+1):
        print("*",end="")
    t.sleep(0.20)
    print()
print()

#using while loop
k=0
while(k<row):
   n=0
   while(n<=k):
    print("*",end="")
    n=n+1
   t.sleep(0.20)
   space=0
   row2=row-k
   while(space<row2-k+row):
    print(" ",end="")
    space=space+1
   o=0
   while(o<=k):
    print("*",end="")
    o=o+1
   t.sleep(0.20)
   print()
   k+=1
