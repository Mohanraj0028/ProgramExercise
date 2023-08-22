n = int(input("Enter :  "))

for i in range(n):
    m = i*i
    if(m==n):
        flag = 0
        break

    else:
        flag = 1
        continue   

if flag == 0:
    print("the number is perfect sq")

else:
    print("not perfect sq")    
