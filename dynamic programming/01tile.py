n = int(input())
lst = [1, 2, 3]
for i in range(3, n):
    lst.append((2*lst[i-2]+lst[i-3])%15746)
print(lst[n-1])
