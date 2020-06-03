import sys

n = int(sys.stdin.readline())
count = 0
a = n

while True:
    a = 10 * (a % 10) + (a // 10 + a % 10) % 10
    count += 1
    if a == n:
        print(count)
        break
