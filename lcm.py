a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
for i in range(2,20):
    if a%i==0 and b%i==0 and c%i==0:
        print(i)
        break
    