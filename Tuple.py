#Declare The Tuple
t=('BCA',2020,8.3,'Rahul',2023)
print("Print Orginal Tuple: ",t)

#Access Value From The Tuple
print("Access The 2 Index From The Tuple: ",t[2])
print("Access 1 TO 4 Index From The Tuple: ",t[1:4])
print("Access Elemrnt From The End: ",t[-4])

#Update The Tuple Elements
#t[0]=3000 This Line Give A Error 
t2=(700,'Timbaliya')
t3=t+t2

print("After The Concate The t And t2: ",t3)

#Deleleting The Tuple
# del t[0] This Line Give A Error YOu Can Delete As Above
del t3

#Basic Tuple Operation
print("Find The length Of The t: ",len(t))

print("Concate The Two Tuple: ",(1,2,3)+(4,5,6))

print("Repeat t 4 Time: ",t*4)

print("Find The Tuple Element: ",'BCA'in t)

t4=(1,2,3,4,5)
print("Used In Loops")
for i in t4:
    print(i)

print("Find The Maximum Element From The Tuple: ",max(t4))
print("Find The Minimum Element From The Tuple: ",min(t4))