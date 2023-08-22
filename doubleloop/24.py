n = int(input("Enter: "))

x = int(input("Enter: "))

sum = 1 
fact = 1
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        
        fact = fact * j
    print(fact)

    temp = x**i/fact
    print(temp)
    sum = sum + temp

print(sum)    
    



