bin = int(input("Enter: "))

rem = []

pro = 0
temp = 0

while bin>0:
    r = bin%10
    rem = rem + [r]
    bin = bin // 10

 


for j in range(len(rem)):

    pro = rem[j] * (2**j) 
    temp = temp + pro

if(temp >9):
    print(chr((temp+55)))

else:
    print(temp)    
    


    
