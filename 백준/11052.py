import sys
import collections
input = sys.stdin.readline

n = int(input())

costs = list(map(int, input().split()))
memo = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        memo[i] = max(memo[i], memo[i - j] + costs[j - 1])

print(memo[-1])
