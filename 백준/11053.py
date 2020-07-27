import sys
import collections
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    maxi = 0
    for j in range(i):
        if arr[j] < arr[i]:
            maxi = max(maxi, dp[j])
    dp[i] = maxi + 1

print(max(dp))
