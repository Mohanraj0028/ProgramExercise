a = [4,3,5,8]

b=[]

k = 0
mul = 1
for i in range(len(a)):
    for j in range(1,a[i]+1):
        
        mul =  mul * j

    print(mul)   
    b = b + [mul]
    mul = 1 
    

print(b)    