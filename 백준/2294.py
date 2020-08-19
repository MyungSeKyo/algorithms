import sys
MAX = 10000000
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [None] * (k + 1)

for coin in coins:
    if 0 <= coin <= k:
        dp[coin] = 1

for i in range(k + 1):

    mini = dp[i] if dp[i] else MAX
    for coin in coins:
        if 0 <= i - coin <= k and dp[i - coin] is not None:
            mini = min(mini, dp[i - coin] + 1)

    if mini != MAX:
        dp[i] = mini

print(dp[k] if dp[k] else -1)
