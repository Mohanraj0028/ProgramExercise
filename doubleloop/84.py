string = input("Enter a string: ")


letter_count = 0
space_count = 0
number_count = 0
other_count = 0


for char in string:
    if ord('a') <= ord(char.lower()) <= ord('z'):
        letter_count += 1
    elif char == ' ':
        space_count += 1
    elif ord('0') <= ord(char) <= ord('9'):
        number_count += 1
    else:
        other_count += 1

# Print the counts
print("Letter count:", letter_count)
print("Space count:", space_count)
print("Number count:", number_count)
print("Other character count:", other_count)
