n=int(input("The number of term's to print: "))

a=0
b=1
c=0

i=1

print(b, end=" ");
while i<=(n-1):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
    i+=1