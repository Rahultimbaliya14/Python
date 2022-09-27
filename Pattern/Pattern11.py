import time as t
#Using For Loop
row=int(input("Enter The Number of The Rows "))
b=1
for a in range(row):
    for c in range(a):
        print(b,end="")
        t.sleep(0.10)
        if b==1:

            b=0
        else:
           b=1
    print()


#Using While Loop


b=1
k=0
while(k<row):
    j=0
    while(j<k):
        print(b,end="")
        t.sleep(0.10)
        if b==0:
            b=1
        else:
            b=0
        j+=1
    print()
    k+=1
