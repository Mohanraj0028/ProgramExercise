n = int(input("Enter: "))
flag = 0

if n == 2 :
    flag = 1

else:
    for i in range(2,n):
        if(n%i==0):
            flag = 0
            break
        else:
            flag = 1

if flag == 1:
    print("Prime")

else:
    print("Not a prime")            