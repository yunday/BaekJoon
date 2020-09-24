import collections

n = int(input())
maze = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for _ in range(n):
    if 1 in maze[_]:
        lst = maze[_].index(1)
        break
queue = collections.deque(lst)