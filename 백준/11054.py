import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]

total = 0
for i in range(n):
    maxi = 0
    maxi2 = 0
    for j in range(i):
        if arr[j] < arr[i]:
            maxi = max(maxi, dp[j][0])
        elif arr[j] > arr[i]:
            maxi2 = max(maxi2, dp[j][1])
    dp[i][0] = maxi + 1
    dp[i][1] = max(maxi2 + 1, maxi + 1)
    total = max(total, dp[i][0], dp[i][1])

print(total)
