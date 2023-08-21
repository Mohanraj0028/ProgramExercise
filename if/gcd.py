n = int(input("Enter the number n :  "))

m = int(input("Enter the number m :  "))


if(n<m):
    min = n
else:
    min = m

for i in range(min,0,-1):

    if n %i ==0 and m % i==0:
        print("gcd is ",i)
        break

