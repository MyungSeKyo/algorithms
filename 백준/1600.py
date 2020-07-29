import sys
import collections
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]

case1 = [
    (-1, -2),
    (-2, -1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (1, 2),
    (2, 1),
]
case2 = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]
queue = collections.deque([(0, 0, k, 0)])
visit = set()


def bfs():
    while len(queue) > 0:
        y, x, remain, depth = queue.popleft()
        if remain > 0:
            for dy, dx in case1:
                if 0 <= y + dy < h and 0 <= x + dx < w and (y + dy, x + dx, remain - 1) not in visit and board[y + dy][x + dx] == 0:
                    if y + dy == h - 1 and x + dx == w - 1:
                        return depth + 1
                    visit.add((y + dy, x + dx, remain - 1))
                    queue.append((y + dy, x + dx, remain - 1, depth + 1))

        for dy, dx in case2:
            if 0 <= y + dy < h and 0 <= x + dx < w and (y + dy, x + dx, remain) not in visit and board[y + dy][x + dx] == 0:
                if y + dy == h - 1 and x + dx == w - 1:
                    return depth + 1
                visit.add((y + dy, x + dx, remain))
                queue.append((y + dy, x + dx, remain, depth + 1))
    return -1
if h == 1 and w == 1:
    print(0)
else:
    print(bfs())
