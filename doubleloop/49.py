n = int(input("Enter "))

for i in range(1, n+1):

    for j in range(n, i, -1):

        print(" ", end="")    
    num = i
    for j in range(1, i+1):
        print(num, end="")
        num += 1
   

    num -= 2
    for k in range(1, i):
        print(num, end="")
        num -= 1
    

    print()