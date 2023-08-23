n = int(input("Enter: "))

f = "black"
for i in range(1, n+1):

    for j in range(1, n+1):
        print(f, end="")
        if j < n:
            print("-", end="")
        if f == "white":
            f = "black"
        else:
            f = "white"
    print() 