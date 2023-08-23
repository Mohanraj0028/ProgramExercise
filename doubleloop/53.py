n = int(input("Enter: "))

for i in range(1,n+1):
    for k in range(n, i, -1):
        print(" ", end="")  
    for j in range(i,0,-1):
        print(j,end=" ")
    print()    