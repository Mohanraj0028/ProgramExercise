n = int(input("Enter: "))
flag = 0

prime = []
count =0
for i in range(2,n+1):
    if i ==2:
        flag = 1
        
    for j in range(2,i):
        if(i%j==0):
            flag = 0
            break

        else:
            flag = 1
            

    if(flag==1):
        
         

        prime = prime + [i]


print(prime)             

for i in range(len(prime)):
    for j in range(len(prime)):
        if(prime[i]+prime[j]== n):
            print(prime[i],prime[j])
            break