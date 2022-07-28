#Pattern 1
print("THis is Statments",end=" ")
row=int(input("Enter The Number Of Rows"))
for i in range(row):
    for space in range(row-i):
          print(" ",end=" ")
    for a in range(i):
      print("*", end="")
    print()