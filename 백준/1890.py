import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

costs = [list(map(int, input().strip().split())) for _ in range(n)]

memo = [[None] * n for _ in range(n)]
memo[0][0] = 1

def recur(y, x):
    if memo[y][x] is not None:
        return memo[y][x]

    ret = 0
    for dx in range(x):
        if costs[y][dx] + dx == x:
            ret += recur(y, dx)

    for dy in range(y):
        if costs[dy][x] + dy == y:
            ret += recur(dy, x)

    memo[y][x] = ret
    return ret

print(recur(n - 1, n - 1))

