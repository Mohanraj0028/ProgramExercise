n = int(input("Enter: "))
flag = 0

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
        
        print(i,end=" ")  
        count = count + 1       
print(count)               