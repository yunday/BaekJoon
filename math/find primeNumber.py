def main():
    n = int(input())
    lst = map(int, input().split())
    cnt = 0
    state = 0
    for i in lst:
        for j in range(2, i//2+1):
            if i % j == 0:
                state = 1
        if state != 1 and i != 1:
            cnt += 1
        state = 0
    print(cnt)


main()
