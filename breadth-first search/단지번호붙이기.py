import collections

n = int(input())
maze = [list(map(int, input())) for _ in range(n)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
id_n, id_m = 0, 0
q_count = [0]*((n * n) // 2)

while True:
    state = 1
    for _ in range(n):
        if 1 in maze[_]:
            id_n = _
            id_m = maze[_].index(1)
            state = 0
            break
    if state == 1:
        break
    queue = collections.deque([[id_n, id_m]])
    cnt += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx == n or tx == -1 or ty == n or ty == -1:
                continue
            if maze[tx][ty] == 1:
                queue.append([tx, ty])
                q_count[cnt-1] += 1
                maze[tx][ty] = cnt + 1

print(cnt)
q_count.sort()
for i in q_count:
    if i != 0:
        print(i)
