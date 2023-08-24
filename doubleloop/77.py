n = int(input("enter: "))

bin = ""

while n>0:
    rem = n%2
    bin = str(rem) + bin
    n = n//2
print(bin)    
