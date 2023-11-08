a=input("Write a string: ")

b=a[: : -1]

print(b)

if a==b:
    print("This is a palindrome")
else:
    print("This is not a palindrome")