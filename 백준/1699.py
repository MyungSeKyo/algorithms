import sys
input = sys.stdin.readline

n = int(input())

dp = [1000000] * (n + 1)
sqrt = [i ** 2 for i in range(1, 318)]
for i in range(min(n, 4)):
    dp[i] = i
for i in range(1, n + 1):

    for j in sqrt:
        if j <= i:
            dp[i] = min(dp[i - j] + 1, dp[i])
print(dp[n])
