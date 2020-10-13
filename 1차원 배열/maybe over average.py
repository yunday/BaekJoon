c = int(input())
for _ in range(c):
    n, *score = map(int, input().split())
    avg = sum(score) / n
    cnt = 0
    for i in score:
        if i > avg:
            cnt += 1
    print('{0:.3f}{1}'.format(round(cnt / n * 100, 3), '%'))
