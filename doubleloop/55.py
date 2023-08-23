n = int(input("Enter: "))


for i in range(n,0,-1):

    for j in range(n, i, -1):

        print(" ", end="")

    for k in range(1, i+1):

        print(k, end="")

    for l in range(i-1, 0, -1):

        print(l, end="")

    print()