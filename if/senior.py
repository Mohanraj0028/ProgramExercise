n = int(input("Enter: "))

m = int(input("Enter:  "))

if(n<25 and m<1):
    print("Entery leve;")

elif(25<=n<40 and 1<=m<5):
    print("junior")

elif(n>40 and 5<m<10):
    print("Senior")    

elif(n>40 and m>10):
    print("Expert")   