arr = [int(input()) for _ in range(9)]
m = max(arr)
print('{0}\n{1}'.format(m, arr.index(m)+1))
print()