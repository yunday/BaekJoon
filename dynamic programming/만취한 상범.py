import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))
for j in range(n):
    print(int(lst[j] ** 0.5))
