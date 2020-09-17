import collections

m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

queue = collections.deque([[i, j] for i in range(n) for j in range(m) if maze[i][j] == 1])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
lx, ly = 0, 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx == n or tx == -1 or ty == m or ty == -1:
            continue
        if maze[tx][ty] == 0:
            queue.append([tx, ty])
            maze[tx][ty] = maze[x][y] + 1
    lx, ly = x, y

state = 0
for _ in maze:
    if 0 in _:
        print(-1)
        state = 1
        break
if state == 0:
    print(maze[lx][ly]-1)

# pop 사용시 제일 앞에꺼를 가져오니까 시간이 오래걸리므로 deque 모듈을 사용!
