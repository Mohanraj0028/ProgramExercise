bin = int(input("Enter: "))

rem = []

while bin>0:
    r = bin%10
    rem = rem + [r]
    bin = bin // 10

print(rem)   
