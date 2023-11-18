list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list1 = list_[5:15:2]
list2 = list_[::4]
sum = avg = 0

print("SLICE 1")
for a in list1:
    sum += a
    print(a, end=" ")

print()

print("Sum of elements of slice 1:", sum)
print("SLICE 2")
sum = 0
for a in list2:
    sum += a
    print(a, end=" ")

print()
avg = sum / len(list2)
print("Average of elements of slice 2:", avg)
