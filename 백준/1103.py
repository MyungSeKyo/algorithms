import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

h, w = map(int, input().split())

board = [list(input().strip()) for _ in range(h)]


case = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]
ret = 0
memo = [[None] * w for _ in range(h)]
visit = set()


def recur(y, x):
    if memo[y][x] is not None:
        return memo[y][x]

    visit.add((y, x))
    memo[y][x] = 0
    for dy, dx in case:
        dy *= int(board[y][x])
        dx *= int(board[y][x])

        if 0 <= y + dy < h and 0 <= x + dx < w and board[y + dy][x + dx] != 'H':
            if (y + dy, x + dx) in visit:
                print(-1)
                exit(0)

            memo[y][x] = max(memo[y][x], recur(y + dy, x + dx) + 1)
    visit.remove((y, x))
    return memo[y][x]

visit.add((0, 0))
recur(0, 0)
print(memo[0][0] + 1)