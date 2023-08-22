n = int(input("ENter: "))

sum = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        sum = sum + 1
        print(sum,end=" ")
    print()    