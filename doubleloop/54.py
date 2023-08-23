n = int(input("Enter: "))


for i in range(1, n+1):

    for j in range(n, i, -1):
        print(" ", end="")

    for k in range(0, i):
        print(2**k, end="")

    for l in range(i-2, -1, -1):
        print(2**l, end="")

    print()