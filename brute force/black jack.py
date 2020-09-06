def main():
    maxi = 0
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if maxi < lst[i]+lst[j]+lst[k] <= m:
                    maxi = lst[i]+lst[j]+lst[k]
    print(maxi)


main()
