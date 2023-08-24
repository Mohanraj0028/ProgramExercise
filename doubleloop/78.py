octal = input("Enter an octal number: ")
decimal = int(octal, 8)  # Convert octal to decimal

hexadecimal = ""

while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
    decimal = decimal // 16

print("Hexadecimal:", hexadecimal)
