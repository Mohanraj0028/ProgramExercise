n = int(input("Enter:  "))
mid = 1
sum = 0

for i in range(1,n+1):
    mid = 10 * mid
    n = mid + 1
    print(n,end=" ")
    sum = sum + n

print(sum)    
