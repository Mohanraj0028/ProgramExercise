n = int(input("Enter: "))

m = int(input("Enter: "))

if(n<m):
    min = n
else:
    min = m

for i in range(2,min+1):
    if(n%i==0 and m%i==0):
        print("gcd",i)

        gcd = i
        break

lcm = (n*m)//gcd

print(lcm)