import sys
import collections
input = sys.stdin.readline

memo = [None] * 5001
memo[0] = 1
memo[1] = 0
memo[2] = 1


def recur(n):
    if memo[n] is not None:
        return memo[n]
    if n % 2 != 0:
        return 0
    # memo[n] = recur(n - 2)
    memo[n] = 0

    for i in range(0, n - 1, 2):
        memo[n] += (recur(i) * recur(n - 2 - i)) % 1000000007
    memo[n] %= 1000000007
    return memo[n]


t = int(input())
for _ in range(t):
    ret = recur(int(input()))
    print(ret)
print()
