#Dictionary Program Example
#Declaring The Dictionary
d={'Name':'Rahul','Department':'BCA','Sem':'5'}
print("Print Original Dictionary: ",d)

#Access Value From The Dictionary
print("Name: ",d['Name'])

print("Department: ",d['Department'])

print("Print Only Keys Value Of The Dictionary: ",d.keys())

print("Print Only Value Of The Dictionary: ",d.values())

print("Print Items Of  The Dictionary: ",d.items())


#Updating Dictionary
d['Sem']=6
print("After Updating Sem: ",d)

d['GPA']=8.3
print("After Adding One Value To Dictionary: ",d)

#Remove Dictionary Element Or Dictionary
del d['GPA']
print("After Deleting GPA From Dictionary: ",d)

#Delete Hole Directory
del d

#More Than One Key Value Same In Dictionary
d={'Name':'Rahul','Department':'BCA','Sem':'5','Name':'TImbaliya'}

print("It Print Last Name Atribute Value: ",d)

'''d={['Name']:'Rahul','Department':'BCA','Sem':'5','Name':'TImbaliya'} This Line Give A Error'''



