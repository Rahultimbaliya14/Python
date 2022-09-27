#Using For Loop
row=int(input("Enter The NUmber Of Rows "))
for i in range(row):
    rowd=row-i
    row2=row*rowd
    for j in range(int(row/2)):
      for space in range(row2-i):
           print(" ",end=" ")
      for a in range(i):
           print("*",end=" ")
      for space in range(row*i):
         print("   ",end=" ")
      for a in range(i):
           print("*",end=" ")
      print()

#Using While Loop

k=0
while(k<row):
   rowd=row-k
   row2=row*rowd
   j=0
   while(j<(int(row/2))):
      r=0
      while(r<row2-k):
         print(" ",end=" ")
         r+=1
      l=0
      while(l<k):
         print("*",end=" ")
         l+=1
      space=0
      while(space<row*k):
         print("   ",end=" ")
         space+=1
      n=0
      while(n<k):
         print("*",end=" ")
         n+=1
      j+=1
      print()
   k+=1
