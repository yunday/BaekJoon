n = int(input())
cnt = 1
lst = sorted([list(map(int, input().split())) for x in range(n)], key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])
end = lst[0][1]
for _ in range(1, n):
    if lst[_][0] >= end:
        cnt += 1
        end = lst[_][1]
print(cnt)
