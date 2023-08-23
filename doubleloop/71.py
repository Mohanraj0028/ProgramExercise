n = int(input("Enter: "))

a = ["A",'B','C','D','E','F']

hexa = ""

while n>0:
    r =  n %16
    if(r>=10):
        hexa = a[r-10]+hexa
    else:
        hexa = str(r)+hexa

    n = n//16    

print(hexa)            