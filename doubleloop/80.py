hexadecimal = input("Enter: ")
decimal = 0
hexadecimal = hexadecimal.upper()  

for digit in hexadecimal:
    if '0' <= digit <= '9':
        decimal = decimal * 16 + int(digit)
    else:
        decimal = decimal * 16 + ord(digit) - ord('A') + 10

print("Decimal:", decimal)
