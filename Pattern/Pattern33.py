#Using For Loop
row=int(input("Enter The Number Of Rows: "))
for i in range(row):
    print(chr(65+i),end=" ")
for j in reversed(range(row)):
    print(chr(65+j),end=" ")
print()
for k in range(row):
    for m in range(row-k):
        print(chr(65+m),end=" ")
    for space in range(k):
        print(" *",end="  ")
    for m in range(row-k):
        print(chr(63+row-m),end=" ")
    print()

print()

#Using While Loop
i=0
while(i<row):
    print(chr(65+i),end=" ")
    i+=1
j=row
while(j>0):
    print(chr(64+j),end=" ")
    j-=1
print()
k=0
while(k<row):
    m=0
    while(m<row-k):
        print(chr(65+m),end=" ")
        m+=1
    space=0
    while(space<k):
        print(" *",end="  ")
        space+=1
    m=0
    while(m<row-k):
        print(chr(63+row-m),end=" ")
        m+=1  
    k+=1  
    print()
