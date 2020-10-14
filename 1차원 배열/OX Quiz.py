n = int(input())
arr = [input().split('X') for _ in range(n)]
for i in range(n):
    print(sum([sum([k for k in range(1, len(j)+1)]) for j in arr[i]]))
