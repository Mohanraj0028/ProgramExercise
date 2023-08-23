n = int(input("Enter: "))

pro = 1

while n > 0 :
    r = n%10
    pro = pro * r
    n = n// 10
print(pro)
    