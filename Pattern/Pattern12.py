import time as t
#Using For Loop
row=int(input("Enter The Number Of Rows "))
for i in range(row):
    for space in range(i):
        print(" ",end=" ")
    for a in range(row-i):
        print("*",end=" ")
    t.sleep(0.20)
    for space1 in range(i):
        print(" ",end="")
    for a1 in range(row-i):
        print("*",end=" ")
    t.sleep(0.20)
    for space2 in range(i):
        print(" ",end="")
    for a3 in range(row-i):
        print("*",end=" ")
    t.sleep(0.20)
    print()

print()

#Using While Loop

j=0
while(j<row):
    spaces=0
    while(spaces<j):
        print(" ",end=" ")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    t.sleep(0.20)
    spaces=0
    while(spaces<j):
        print(" ",end="")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    t.sleep(0.20)
    spaces=0
    while(spaces<j):
        print(" ",end="")
        spaces=spaces+1
    k=0
    while(k<row-j):
        print("*",end=" ")
        k+=1
    t.sleep(0.20)
    print()
    j+=1