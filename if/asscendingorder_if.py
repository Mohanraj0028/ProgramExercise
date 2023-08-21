a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a<b and a < c):
    print(a,end=" ")
    if(b<c):
        print(b,c)
    else:
        print(c,b)

elif(b<a and b < c):
    print(b,end=" ")
    if(a<c):
        print(a,c)
    else:
        print(c,a)

elif(c<a and c < b):
    print(c,end=" ")
    if(a<b):
        print(a,b)
    else:
        print(b,a)

