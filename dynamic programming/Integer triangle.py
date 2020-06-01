import sys

n = int(sys.stdin.readline())
tri = [[int(sys.stdin.readline())]]
L = [[-1]]
for a in range(1, n):
    tri.append(list(map(int, sys.stdin.readline().split())))
    L.append([-1] * (a + 1))


def triangle():
    for i in range(n):
        for j in range(i+1):
            if i == 0 and j == 0:
                L[i][j] = tri[i][j]
            elif j == 0:
                L[i][j] = L[i - 1][j] + tri[i][j]
            elif j == i:
                L[i][j] = L[i - 1][j - 1] + tri[i][j]
            else:
                L[i][j] = max(L[i - 1][j - 1], L[i - 1][j]) + tri[i][j]
    maxvalue = L[n - 1][0]
    for i in range(1, n):
        maxvalue = max(maxvalue, L[n - 1][i])
    return maxvalue


print(triangle())
