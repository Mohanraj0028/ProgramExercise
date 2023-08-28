def findmax(numbers):
    if not numbers:
        return None

    max = numbers[0]
    for i in numbers:
        if i > max:
            max_value = i

    return max_value


numbers = [23, 45, 12, 67, 89, 54]
maximum = findmax(numbers)
print("Maximum:", maximum)
