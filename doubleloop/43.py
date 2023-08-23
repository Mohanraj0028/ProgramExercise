n = int(input("Enter: "))

for i in range(1,n+1):
    if(i%2==0):
        p = 0
        q = 1
    else:
        q = 0
        p = 1

    for j in range(1,i+1):
        if(j%2==0):
            print(q,end="")

        else:
            print(p,end="")  

    print()              
