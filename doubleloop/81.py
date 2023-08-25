hexa = input("Enter a hexadecimal number: ")
deci = 0
i = len(hexa) - 1

# Convert hexadecimal to decimal
for i in hexa:
    if '0' <= i <= '9':
        deci += int(i) * (16 ** len(hexa) - 1 - i)
    else:
        deci += (ord(i) - ord('A') + 10) * (16 ** len(hexa) - 1 - i)

octal = ""
j = 0

# Convert decimal to octal
while deci > 0:
    remainder = deci % 8
    octal = str(remainder) + octal
    deci = deci // 8
    j += 1

print("Octal:", octal)
