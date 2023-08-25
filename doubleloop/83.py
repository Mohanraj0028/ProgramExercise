
number = int(input("Input any number: "))


sum = 0
num_str = str(abs(number))  

for i in num_str:
    sum += int(i)


print(sum)
