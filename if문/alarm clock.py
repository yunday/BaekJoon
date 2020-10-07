h, m = map(int, input().split())
m -= 45
if m < 0:
    if h == 0:
        h = 23
    else:
        h -= 1
    m += 60
print(h, m)