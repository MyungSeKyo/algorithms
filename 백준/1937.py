import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
memo = [[None] * n for _ in range(n)]
case = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]
def dp(y, x):
    if memo[y][x] is not None:
        return memo[y][x]

    memo[y][x] = 0
    for dy, dx in case:
        if 0 <= y + dy < n and 0 <= x + dx < n:
            if costs[y + dy][x + dx] < costs[y][x]:
                memo[y][x] = max(dp(y + dy, x + dx), memo[y][x])
    memo[y][x] += 1
    return memo[y][x]

ret = 0
for i in range(n):
    for j in range(n):
        dp(i, j)
        ret = max(ret, memo[i][j])
print(ret)