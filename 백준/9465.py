import sys
import collections

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    memo = [[0] * 3 for _ in range(n)]
    memo[0] = [0, board[0][0], board[1][0]]
    for i in range(1, n):
        memo[i][0] = max(memo[i - 1])
        memo[i][1] = max(memo[i - 1][2], memo[i - 1][0]) + board[0][i]
        memo[i][2] = max(memo[i - 1][1], memo[i - 1][0]) + board[1][i]
    print(max(memo[-1]))