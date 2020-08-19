import sys
import collections
input = sys.stdin.readline

w, h = map(int, input().split())

board = [list(input().strip()) for _ in range(h)]

m1 = None
m2 = None

for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            if m1:
                m2 = (i, j)
            else:
                m1 = (i, j)

queue = collections.deque([(*m1, 0, 0, 0)])
visit = {}
case = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]
while len(queue) > 0:
    y, x, by, bx, depth = queue.popleft()

    if (y, x) == m2:
        print(depth)
        exit()

    for dy, dx in case:
        if (y + dy, x + dx, y, x) not in visit or visit[(y + dy, x + dx, y, x)] > depth:
            if 0 <= y + dy < h and 0 <= x + dx < w and (y + dy, x + dx) != m1:
                if board[y + dy][x + dx] in ('.', 'C'):
                    if y - by == dy and x - bx == dx or (y, x) == m1:
                        visit[(y + dy, x + dx, y, x)] = depth
                        queue.appendleft((y + dy, x + dx, y, x, depth))
                    else:
                        visit[(y + dy, x + dx, y, x)] = depth + 1
                        queue.append((y + dy, x + dx, y, x, depth + 1))