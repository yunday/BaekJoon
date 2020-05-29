import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lst = [arr[0]]
sumMax = lst[0]
mini = lst[0]

for i in range(1, n):
    lst.append(lst[i-1] + arr[i])
    mini = min(mini, lst[i - 1])
    if mini < 0:
        sumMax = max(sumMax, lst[i] - mini)
    else:
        sumMax = max(sumMax, lst[i])

print(sumMax)
