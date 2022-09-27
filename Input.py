#Input Is Used To Read The Input From User
print("\n*********Find Number Is Odd Or Even*********\n")

#Integer Input
#This Statement Read The Value From User 
A=int(input("Enter The First Number:  "))

if(A%2 == 0):
    print("Number Is Even")
else:
    print("Number Is Odd")

#Float Input
B=float(input("Enter The Float Number"))
print(B)

#Array Input
E=int(input("Enter A Element Of Array"))
array=[]

for i in range(E):
    array.append(int(input("Enter the Array Element: ")))

print(array)
