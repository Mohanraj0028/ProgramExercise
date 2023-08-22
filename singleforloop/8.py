n = "Hai i am mohan"

count = 0

small  = n.lower()

print(small)

for i in range(len(n)):
    if(small[i]=="a" or small[i]=="e" or small[i]=="i" or small[i]=="o" or small[i]=="u"):
        count = count + 1
        continue

print(count)    

