import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dp = [[None, None, None] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [1, 1, 1]


def recur(n):
    if dp[n][0] is not None:
        return sum(dp[n])

    recur(n - 1)
    recur(n - 2)
    recur(n - 3)
    dp[n][0] = dp[n - 1][0]
    dp[n][1] = dp[n - 2][0] + dp[n - 2][1]
    dp[n][2] = sum(dp[n - 3])
    return sum(dp[n])

t = int(input())

for _ in range(t):
    num = int(input())
    print(recur(num))
