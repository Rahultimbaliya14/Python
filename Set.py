#Declare The Set
#Using Set Method
a=set([220,'BCA','Dhari','2002'])
print(a)
#Using {} Brackets
b={220,'BCA','Dhari','2002','Rahul',220,'Timbaliya',8,2022}
print(b)

#Access The Set Element Using Only For Loop
for i in a:
    print(i)

#Add Items To The Set
a.add(1000)
print("After Adding Element To The Set",a)

#Remove The Element From The Set
a.remove('BCA')
print("After Removing Element From The Set",a)

c=a|b
print("After The Union Of The Two Set",c)

c=a&b
print("After Intersection Of The Two Set",c)

c=a-b
print("After Find Difference Of Two Set",c)

#Compare The Set
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)