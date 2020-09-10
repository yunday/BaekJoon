n = int(input())
cnt = 0

for i in range(666, 2700000):
    if "666" in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
