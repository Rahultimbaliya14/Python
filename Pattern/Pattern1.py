import time as t

#Pattern 1 With help Of For Loop
row=int(input("Enter The Number Of Rows"))
for i in range(row):
    for space in range(row-i):
          print(" ",end="")
    for a in range(i+1):
      print("* ",end="")
      t.sleep(0.10)
    print()

#With Help Of While Loop
j=0
while(j<=row):
      spaces=0
      b=0
      while(spaces<=row-j):
            print(" ",end="")
            spaces=spaces+1
      while(b<=j-1):
             print("* ",end="")
             t.sleep(0.10)
             b=b+1
      j=j+1
      print()

