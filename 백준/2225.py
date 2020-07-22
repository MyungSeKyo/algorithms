import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n += 1
dp = [[0] * n for _ in range(k)]
dp[0] = [1] * n
for i in range(1, k):
    for j in range(n):
        dp[i][j] = sum(dp[i - 1][:j + 1]) % 1000000000

print(dp[-1][-1])