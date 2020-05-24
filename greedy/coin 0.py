import sys

a = sys.stdin.readline().split()
n = int(a[0])
k = int(a[1])

lst = []
for i in range(n):
    o = int(sys.stdin.readline())
    if o < k:
        lst.append(o)
count = 0
for x in lst[::-1]:
    count += k//x
    k -= ((k//x) * x)
    if k == 0:
        break

print(count)