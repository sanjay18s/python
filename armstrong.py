a=int(input("enter the value: "))
n=0
while(a>0):
    r=a%10
    n=(n)+r**3
    a=a//10
print(n)
 
