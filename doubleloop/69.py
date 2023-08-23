n = int(input("Enter:  "))

for i in range(n):
    for j in range(n):
        value  =  i-j

        if(value<0):
            value = value * -1
            print(value,end=" ")
        else:
            print(value,end=" ")    

    print()        