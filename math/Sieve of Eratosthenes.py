def main():
    lst = [False, False] + [True]*1000000
    for i in range(2, int(1000000 ** 0.5)):
        if lst[i]:
            for j in range(i * 2, len(lst), i):
                lst[j] = False
    m, n = map(int, input().split())
    a = [x for x in range(m, n+1) if lst[x]]
    print(*a, sep="\n")


main()
