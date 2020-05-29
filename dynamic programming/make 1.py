import sys

n = int(sys.stdin.readline())


def find():
    d = [0 for _ in range(n + 1)]
    for k in range(2, n+1):
        d[k] = d[k-1] + 1
        if k % 3 == 0:
            d[k] = min(d[k//3] + 1, d[k])
        if k % 2 == 0:
            d[k] = min(d[k//2] + 1, d[k])
    print(d[n])


find()

