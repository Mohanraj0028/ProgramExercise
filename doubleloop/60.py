a = ["zero","one","two","three","four","five","six","seven","eight","nine"]

n = int(input("Enter: "))

rem = []

while n > 0 :
    r = n%10
    
    n = n// 10
    

    rem = rem + [r] 




for i in range(len(rem)-1,-1,-1):
    print(a[rem[i]],end=" ")