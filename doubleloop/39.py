n = int(input("Enter: "))

num = 1

for i in range(1, n + 1):

    print(" " * (n - i), end="")

    for j in range(i):

        print(num, end=" ")

        num += 1

    print()