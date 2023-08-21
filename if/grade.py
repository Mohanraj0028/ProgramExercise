a = int(input("Enter:  "))
b = int(input("Enter:  "))
c = int(input("Enter:  "))
d = int(input("Enter:  "))
e = int(input("Enter:  "))

sum = a+b+c+d+e

per = (sum/500) * 100

print(per)

if(per >= 90):
    print("gread A")

elif(per >=80):
    print("gread B")    

elif(per >= 70):
    print("grade C")

elif(per >= 60):
    print("Grade D")

elif(per >= 50):
    print("Grade E") 

elif(per >=40):
    print("Grade F")
