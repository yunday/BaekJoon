def main():
    lst = [False, False] + [True]*123456*2
    for i in range(2, int((123456*2) ** 0.5)):
        if lst[i]:
            for j in range(i * 2, len(lst), i):
                lst[j] = False
    p = []
    while True:
        n = int(input())
        if n == 0:
            break
        a = [x for x in range(n+1, 2*n+1) if lst[x]]
        p.append(len(a))
    print(*p, sep='\n')


main()
