n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 권오흠 교수님이 말씀하셨지.... 미로는 방향을 체크해야한다고

data_queue = [[0, 0]]
visited = [[0]*m for i in range(n)]
visited[0][0] = 1

while data_queue:
    x, y = data_queue.pop(0)
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx == -1 or ty == -1 or tx == n or ty == m:
            continue
        if visited[tx][ty] == 0 and maze[tx][ty] == 1:
            visited[tx][ty] = visited[x][y] + 1
            data_queue.append([tx, ty])

print(visited[n-1][m-1])
