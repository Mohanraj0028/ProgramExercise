binary = input("Enter: ")
binary = binary.lstrip('0')

while len(binary) % 3 != 0:
    binary = '0' + binary

octal_mapping = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7"
}

octal = ""

for i in range(0, len(binary), 3):
    group = binary[i:i+3]
    octal_digit = octal_mapping[group]
    octal += octal_digit

print("Octal:", octal)
