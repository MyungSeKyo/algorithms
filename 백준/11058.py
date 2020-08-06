import sys
import collections
input = sys.stdin.readline

n = int(input())
dp = [0] * 100
dp[0] = 1
dp[1] = 2
dp[2] = 3
for i in range(3, 100):
    dp[i] = dp[i - 1] + 1
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i - j] * (j - 1))
    dp[i] = dp[i]
print(dp[n - 1])