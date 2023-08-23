n = int(input("Enter: "))

pro = 1

rem = [0,1,2,3,4,5,6,7,8,9]

while n > 0 :
    r = n%10
    pro = pro * r
    n = n// 10
    print(r)
    rem[r] =  rem[r]+1

print(rem)   

for i in range(len(rem)):
    print(i,"frequency is", rem[i]-i)