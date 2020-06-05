n = int(input())
cnt = n
i = 0

while n - 5*i >= 0:
    if (n - 2*i) % 3 == 0:
        cnt = min(cnt, (n - 2*i)//3)
    i += 1

if cnt == n:
    cnt = -1
print(cnt)
