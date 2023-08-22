n = int(input("Enter: "))

sum = 0
while n != 0 :
    rem = n%10
    sum =sum + int(rem)
    n = n/10

print(int(sum))   
