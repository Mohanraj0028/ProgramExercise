n = int(input("Enter: "))


for i in range(1, n+1):

    for j in range(n, i, -1):

        print(" ", end="")

    for k in range(1, i+1):

        print(chr(k+64), end="")

    for l in range(i-1, 0, -1):

        print(chr(l+64), end="")

    print()