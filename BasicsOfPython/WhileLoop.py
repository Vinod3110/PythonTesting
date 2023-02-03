a = 10
print("===============================")
while a>1:
    if a % 2 != 0:
        a = a - 1
        continue
    if a == 3:
        break
    print(a)
    a = a - 1
print("===============================")
