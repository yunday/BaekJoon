def main():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    for j in lst:
        dist = ((j[0]-j[3])**2 + (j[1]-j[4])**2)**0.5
        r1 = j[2]
        r2 = j[5]
        if r2 < r1:
            r1 = j[5]
            r2 = j[2]
        if r2 == r1 and dist == 0:
            print(-1)
        elif r2 - r1 < dist < r2 + r1:
            print(2)
        elif dist == r2 - r1 or dist == r2 + r1:
            print(1)
        elif r1 + r2 < dist or dist < r2 - r1:
            print(0)


main()
