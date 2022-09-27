import time as t
#Pattern5.py
#Using For Loop
row=int(input("Enter The Number Of Rows"))
for i in range(row):
    for space in range(row-i):
          print(" ",end="")
    for a in range(i+1):
      print("* ",end="")
    t.sleep(0.20)
    print()
j=row
for i in range(row):
    for spaces in range(i+1):
        print(" ",end="")
    for a in range(j):
        print("* ",end="")
    t.sleep(0.20)
    j=j-1
    print()

#Using While Loop
e=0
while(e<=row):
      spaces2=0
      b=0
      while(spaces2<=row-e):
            print(" ",end="")
            spaces2=spaces2+1
      while(b<=e-1):
             print("* ",end="")
             b=b+1
      t.sleep(0.20)
      e=e+1
      print()
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
    t.sleep(0.20)
    k=k-1
    m=m+1
    print()