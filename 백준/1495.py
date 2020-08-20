import sys
input = sys.stdin.readline

n, s, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))
arr = [0] + arr
dp = [set() for _ in range(n + 1)]
dp[0].add(s)

for i in range(1, n + 1):
    for before in dp[i - 1]:
        if 0 <= before + arr[i] <= m:
            dp[i].add(before + arr[i])
        if 0 <= before - arr[i] <= m:
            dp[i].add(before - arr[i])

if dp[-1]:
    print(sorted(dp[-1])[-1])
else:
    print(-1)
