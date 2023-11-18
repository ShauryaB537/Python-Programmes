# Making the abnormally large


list_ = [1, 2, 3, 4, 5, 6, 7]

l = len(list_)

if l % 2 == 0:
    print("HALF-1")
    L1 = list_[: (l // 2)]
    print(L1)
    print("HALF-2")
    L2 = list_[(l // 2) :]
    print(L2)
else:
    print("HALF-1")
    L1 = list_[: ((l + 1) // 2)]
    print(L1)
    print("HALF-2")
    L2 = list_[((l - 1) // 2) :]
    print(L2)
