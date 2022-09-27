#Using For Loop
str=input("Enter The String")
len=len(str)
for i in range(len+1):
    for space in range(len-i): 
        print(" ",end="")
    for a in range(i):
        print(str[a],end=" ")
    print()

print()
#Using While Loop
l=0
while(l<=len):
    j=0
    while(j<len-l):
        print(" ",end="")
        j+=1
    m=0
    while(m<l):
        print(str[m],end=" ")
        m+=1
    l+=1
    print()
