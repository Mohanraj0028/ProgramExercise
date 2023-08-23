n = int(input("enter: "))

oct = ""

while n>0:
    rem = n%8
    oct = str(rem) + oct
    n = n//8
print(oct)    
