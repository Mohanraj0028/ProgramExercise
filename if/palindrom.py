n = "mam"

print(len(n))

for i in range(len(n)):
    print(n[len(n)-i-1])
    if(n[i]== n[len(n)-i-1]):
        flag = 0
        continue
    else:
        flag = 1
        break

if flag == 0:
    print("palindrom")

else:
    print("not palindrom")