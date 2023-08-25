n = int(input("Enter: "))


def fact(a):
    pro = 1
    for i in range(1,a+1):
        pro = pro * i

    return pro

print(fact(n))