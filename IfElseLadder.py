from tokenize import Double
print("*******Welcome********\n")
name=input("Enter The Student Name\n")
mark1=int(input("Enter The First Subject Mark\n"))
mark2=int(input("Enter The Second Subject  Mark\n"))
mark3=int(input("Enter The Third Subject Mark"))

total=mark1+mark2+mark3

pr=total/3

if pr<=35 :
    grade="You Are Fail"
elif pr>=36 and pr<=45 :
    grade="You Are Got A D Grade "
elif pr>=45 and pr<=55 :
    grade="You Got A C Grade"
elif pr>=55 and pr<=65 :
    grade="You Got A B Grade"
elif pr>=65 and pr<=85 :
    grade="You Got A A Class"
elif pr>=85 and pr<=99 :
    grade="You Got A A+ Class"
else :
    print("Enter The Right Choice....")

print()

print("**********Detail************\n")
print("Student Name : ",name,)
print("Subject 1 Mark : ",mark1)
print("Subject 2 Mark : ", mark2)
print("Subject 3 Mark : ",mark3)

print()

print("****Total & PR & GRADE****")
print("Total : ", total)
print("PERSENTAGE : ",pr)
print("Grade : ",grade)

