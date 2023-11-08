sum=0
n=int(input("Sum tillw hich term: "));

for i in range(1, (n+1)):
    for a in range(1, (i+1)):
        sum+=a
print(sum)