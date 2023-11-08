n=int(input("Upto which the sum is needed: "));

e=0
o=0

for i in range(1, (n+1)):
    if i%2==0:
        e+=i
    else:
        o+=i
print("Sum of even numbers till", n, "is", e)
print("Sum of odd numbers till", n, "is", o)