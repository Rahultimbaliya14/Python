#String DataType Example
#Asign Value To a1 And a2
a1="Rahul Timbaliya"
a2="BCA Student"

#Accesing Value From a1 And a2
print(a1[3])
print(a2[5:8])

#Updating The String
print(a1[:15]+""+a2)

#Escape Character
print("\a \t"+a1+" \b\n"+a2+"\e")

#Special Operator
print("(+)Concate Opearator:  "+a1+a2)
print("(*) Repetation Opearator:  "+a1*2)
print("([]) Slice Opearator:  "+a1[4])
print("([:]) Slice With Range Opearator:  "+a2[3:8])
print('R' in a1)
print('R' not in  a1)
print("([r]) Print The Escape Chaeacter Opearator:  "+"heelow"r'\n'"hoi"r'\t'"now")

#String Formation
 
print("My Name Is %s I am Study On %d Sem Of %s My Current Gpa Is %g"%('Rahul',5,'BCA',8.3))

#Unicode String 

print(u"My Name Is Rahul Timbaliya")



