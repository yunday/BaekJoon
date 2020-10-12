n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
s = 0
for i in range(n):
    s += arr[i]/max_value*100
print(s/n)
