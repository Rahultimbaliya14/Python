import pyautogui as v
import time as t
row=int(input("Enter The Number Of Rows: "))

for i in range(row+1):
    for space in range(row*3-i):
        print(" ",end="")
    t.sleep(0.25)
    print("*",end="")
    for innersace in range(i):
        print("*",end="*")
    t.sleep(0.25)
    print("*",end="")
    print()

for a in range(row*2):
    print("*",end="")
t.sleep(0.25)
for space in range(row*2+2):
    print(" ",end="")
for a in range(row*2):
    print("*",end="")
t.sleep(0.25)

print()
for i in range(row):
    for space in range(i):
        print(" ",end="") 
    t.sleep(0.25)
    print("*",end="")
    for space in range(row*6-i-i):
        print(" ",end="")
    t.sleep(0.25)
    print("*",end="")
    print()

for c in range(row):
    for space in range(row-c):
        print(" ",end="")
    t.sleep(0.25)
    print("*",end="")
    for b in range(row*4+c+c):
        print(" ",end="")
    t.sleep(0.25)
    print("*",end="")   
    print()

for a in range(row*2):
    print("*",end="")
for space in range(row*2+2):
    print(" ",end="")
for a in range(row*2):
    print("*",end="")

print()
for i in range(row+1):
    for space in range(row*2+i):
        print(" ",end="")
    t.sleep(0.25)

    print("*",end="")
    for innerspace in range(row*2-i-i):
        print("*",end="")
    t.sleep(0.25)
    print("*",end="")
    print()
 


print()


#Using While Loop
i=0
while(i<row+1):
    space=0
    while(space<row*3-i):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<i):
        print("*",end="*")
        innerspace+=1
    print("*",end="")
    i+=1
    print()

a=0
while(a<row*2):
    print("*",end="")
    a+=1
space=0
while(space<row*2+2):
    print(" ",end="")
    space+=1
a=0
while(a<row*2):
    print("*",end="")
    a+=1
print()

i=0
while(i<row):
    space=0
    while(space<i):
        print(" ",end="")
        space+=1
    print("*",end="")
    space=0
    while(space<row*6-i-i):
        print(" ",end="")
        space+=1
    print("*",end="")
    i+=1
    print()

c=0
while(c<row):
    space=0
    while(space<row-c):
        print(" ",end="")
        space+=1
    print("*",end="")
    b=0
    while(b<row*4+c+c):
        print(" ",end="")
        b+=1
    print("*",end="")
    c+=1
    print()

a=0
while(a<row*2):
    print("*",end="")
    a+=1
space=0
while(space<row*2+2):
    print(" ",end="")
    space+=1
a=0
while(a<row*2):
    print("*",end="")
    a+=1
print()

i=0
while(i<row+1):
    space=0
    while(space<row*2+i):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<row*2-i-i):
        print("*",end="")
        innerspace+=1
    print("*",end="")
    i+=1
    print()
    