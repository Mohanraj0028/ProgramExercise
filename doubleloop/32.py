fir = int(input("Enter first: "))
diff = int(input("Enter common: "))
n = int(input("Enter no of terms: "))
sum = fir
total = fir
print(fir,end=" ")
for i in range(1,n):
    print()

    sum = sum*diff
    print(sum,end=" ")

    total  = total + sum

print()    
print(total)    