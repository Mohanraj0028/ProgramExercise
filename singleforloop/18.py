a = [1,2,3,4,56,7]
b = [1,3,7]
new = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            print(a[i])
            new.append(a[i])
print(new)


            

