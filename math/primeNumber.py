def main():
    m = int(input())
    n = int(input())
    state = 0
    lst = []
    for i in range(m, n+1):
        for j in range(2, i//2+1):
            if i % j == 0:
                state = 1
                break
        if state == 0 and i != 1:
            lst.append(i)
        state = 0
    if lst:
        print(sum(lst), lst[0], sep='\n')
    else:
        print(-1)


main()
