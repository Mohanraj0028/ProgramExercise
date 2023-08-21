x = int(input("Enter:  "))
y = int(input("Enter:  "))
z = int(input("Enter:  "))

if(x==y==z):
    print("Equaliteral triangle")

elif(x==y or y==z or x==z):
    print("isosceles")

else:
    print("Scalene")   
