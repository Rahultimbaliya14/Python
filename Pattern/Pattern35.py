#Using For Loop
row=int(input("Enter The Number Of The Rows: "))
for i in range(row+1):
   for a in range(i):
     print(chr(64+i)+" * ",end="")
   print()
b=0
for j in reversed(range(row)):
    for a  in range(j):
        print(chr(64+j)+" * ",end="")
        b+=1
    print()

#Using While Loop
i=0
while(i<row):
    a=0
    while(a<i):
        print(chr(64+i)+" * ",end="")
        a+=1
    print()
    i+=1
b=0
j=row
while(j>0):
    a=0
    while(a<j):
        print(chr(64+j)+" * ",end="")
        a+=1
        b+=1
    print()
    j-=1

