import sys

put = sys.stdin.readline().split()
a = int(put[0])
b = int(put[1])
c = int(put[2])

if c > b:
    print(a//(c-b)+1)
else:
    print(-1)
