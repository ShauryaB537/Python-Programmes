string=input("Write a string: ")
length=len(string)

string2=""

for a in range(0, length):
    if a%2!=0:
        string2+=string[a].capitalize()
    else:
        string2+=string[a]

print(string2)