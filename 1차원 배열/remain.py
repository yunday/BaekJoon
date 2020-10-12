arr = [int(input()) for _ in range(10)]
lst = []
for _ in range(10):
    remain = arr[_] % 42
    if remain in lst:
        continue
    lst.append(remain)
print(len(lst))
