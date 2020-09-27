import collections

n = int(input())
maze = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q_count = []


def bfs(id_n, id_m):
    queue = collections.deque([[id_n, id_m]])
    maze[id_n][id_m] = 0
    p_count = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            tx = x + dx[k]
            ty = y + dy[k]
            if tx == n or tx == -1 or ty == n or ty == -1:
                continue
            if maze[tx][ty] == 1:
                queue.append([tx, ty])
                p_count += 1
                maze[tx][ty] = 0
    return p_count + 1


for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            q_count.append(bfs(i, j))

print(len(q_count))
print(*sorted(q_count))
