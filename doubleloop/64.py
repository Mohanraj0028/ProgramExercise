n = int(input("Enter: "))

bit = []

while n > 0:
     r = n%10
     
     n = n//10
     bit = bit + [r]


for j in range(len(bit)-1,-1,-1):
     
     if bit[j] == 0:
          print(1,end="")
     else:
          print(0,end="")     
     