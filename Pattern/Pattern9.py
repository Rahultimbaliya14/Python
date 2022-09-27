import time as t
#Using For Loop
row=int(input("Enter The Number Of Rows"))
j=row
for i in range(row):
    for space in range(i):
        print(" ",end="")
    for a in range(j):
        print("* ",end="")
    t.sleep(0.20)
    j=j-1
    print()
for i in range(row):
    for space in range(row-i-1):
          print(" ",end="")
    for a in range(i+1):
      print("* ",end="")
    t.sleep(0.20)
    print()

print()


#Using While Loop
k=row
m=0
while(m<row):
    spaces=0
    while(spaces<m):
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
j=1
while(j<=row):
      spaces=0
      b=0
      while(spaces<row-j):
            print(" ",end="")
            spaces=spaces+1
      while(b<=j-1):
             print("* ",end="")
             b=b+1
      t.sleep(0.20)
      j=j+1
      print()

