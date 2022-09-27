#Using For Loop
from turtle import end_fill


row=int(input("Enter The Number Of Rows "))
for a in range(row*4):
    print(" ",end="")
print("*")
for i in range(row-1):
    for space in range(row*4-2):
        print(" ",end="")
    print("*",end="")
    for space in range(4):
        print(" ",end="")
    print("*",end="")
    print()
for space in range(row):
    print(" ",end=" ")
for b in range(row):
    print("*",end=" ")
for space in range(3):
    print(" ",end="")  
for b in range(row):
    print("*",end=" ")  
print()
for space in range(row*2-2):
    print(" ",end="")
print("*",end="")
for space in range(row*4+4):
    print(" ",end="")
print("*",end="")
print()
for space in range(row):
    print(" ",end=" ")
for b in range(row):
    print("*",end=" ")
for space in range(3):
    print(" ",end="")  
for b in range(row):
    print("*",end=" ")  
print()

for i in range(row):
    for space in range(row*4-2):
        print(" ",end="")
    print("*",end="")
    for innerspace in range(4):
        print(" ",end="")
    print("*",end="")
    print()
for a in range(row*4):
    print(" ",end="")
print("*")

#Using While Loop
a=0
while(a<row*4):
    print(" ",end="")
    a+=1
print("*")
i=0
while(i<row-1):
    space=0
    while(space<row*4-2):
        print(" ",end="")
        space+=1
    print("*",end="")
    space=0
    while(space<4):
        print(" ",end="")
        space+=1
    print("*",end="")
    i+=1
    print()  


space=0
while(space<row):
    print(" ",end=" ")
    space+=1
b=0
while(b<row):
    print("* ",end="")
    b+=1
space=0
while(space<3):
    print(" ",end="")
    space+=1
b=0
while(b<row):
    print("* ",end="")
    b+=1
print()

space=0
while(space<row*2-2):
    print(" ",end="")
    space+=1
print("*",end="")
space=0
while(space<row*4+4):
    print(" ",end="")
    space+=1
print("*",end="")

print()

space=0
while(space<row):
    print(" ",end=" ")
    space+=1
b=0
while(b<row):
    print("* ",end="")
    b+=1
space=0
while(space<3):
    print(" ",end="")
    space+=1
b=0
while(b<row):
    print("* ",end="")
    b+=1
print()

i=0
while(i<row):
    space=0
    while(space<row*4-2):
        print(" ",end="")
        space+=1
    print("*",end="")
    innerspace=0
    while(innerspace<4):
        print(" ",end="")
        innerspace+=1
    print("*",end="")
    i+=1
    print()
a=0
while(a<row*4):
    print(" ",end="")
    a+=1
print("*")