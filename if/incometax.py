n = int(input("Enter: "))

if (n<=10000):
    print("no tax")

elif(n<=25000):
    print("low tax bracket")

elif(n<=40000):
    print("middle tax bracket")

else:
    print("high bracket income")        