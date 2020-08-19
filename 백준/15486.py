import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

costs = []
benefits = []

for _ in range(n):
    t, p = map(int, input().split())
    costs.append(t)
    benefits.append(p)

dp = [0] * (n * 10)
maxi = 0
for i in range(n):
    if i + costs[i] - 1 < n:
        dp[i + costs[i] - 1] = max(dp[i + costs[i] - 1], maxi + benefits[i])
    maxi = max(dp[i], maxi)
print(max(dp))
