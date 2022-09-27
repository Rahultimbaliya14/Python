#Declare The list
a=[2,5,5,8.3]
print("Print Original List: ",a)

#Opearation On The List
a.insert(1,2020)
print("After Inserting One Value On The List: ",end=" ")
print(a)

a.append(2023)
print("After Append One value TO The List: ",end=" ")
print(a)

print("Count Element From The List: "+str(a.count(2020)))

print("Find The Index Of The List Element: "+str(a.index(5)))

a.sort()
print("After Sort The List: ",a)

a.reverse()
print("After The Reverse The List: ",a)

a.remove(2020)
print("After The Removing One Element From The List: ",a)

a.pop(2)
print("After The Pop One Element From The List: ",a)

b=['BCA',8.3]
a.extend(b)
print("After Extending List: ",a)

#Access Value From List

print("The Access 4 Index From The List: ",a[4])
print("Access The 0 To 4 Element From The List: ",a[0:4])

#Updating The List
a[3]=500
print("After The Upadate 3 Index From The List: ",a)

#Delete From The List
del a[5]
print("After The Delelting 5 index From The List: ",a)


