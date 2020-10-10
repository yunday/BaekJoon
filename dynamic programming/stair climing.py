n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
result = [[stair[0]], [stair[1], stair[0]+stair[1]]]
dif = 1
for i in range(2, n):
    result.append([x+stair[i] for x in result[0]])
    for j in range(len(result[1])-dif):
        result[2].append(result[1][j]+stair[i])
    dif = len(result[1])-dif
    del result[0]
print(max(result[1]))
