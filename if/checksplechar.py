str = input("Enter the char: ")

n = str.upper()

if(56<ord(n)<90):
    print("is alphabet")

elif(48<ord(n)<57):
    print("is number")

else:
    print("is specialchat")   