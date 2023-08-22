a = ["hai","MOHan","apple"]

for i in range(len(a)):
    
    lower = a[i].lower()
    if(lower[0] == "a" or lower[0] == 'e' or lower[0] == "i" or lower[0] == "o" or lower[0] == "u"):
        print(a[i])