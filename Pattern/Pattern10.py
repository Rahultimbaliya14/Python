import math
import time as t
from pkg_resources import ensure_directory
row=int(input("Enter The NUmber Of Rows"))
d=math.ceil(row/2)
for i in range(row+1):
    for a in range(row+1):
        if i+a==d or a-i==d or i-a==d or i+a==row+d:
            print("*",end="")
            t.sleep(0.20)
        else:
            print(" ",end="")
    print()
print()

#Using While Loop
j=0
while(j<=row):
    k=0
    while(k<=row):
        if j+k==d or k-j==d or j-k==d or j+k==row+d:
            print("*",end="")
            t.sleep(0.20)
        else:
            print(" ",end="")
        k+=1
    j+=1
    print()
