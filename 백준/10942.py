import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

dp = [[None] * n for _ in range(n)]

t = int(input())


def recur(i, j):
    if dp[i][j] is not None:
        return dp[i][j]

    if i == j:
        dp[i][j] = True
        return True

    if i + 1 == j:
        if arr[i] == arr[j]:
            dp[i][j] = True
            return True
        else:
            dp[i][j] = False
            return False

    if recur(i + 1, j - 1) and arr[i] == arr[j]:
        dp[i][j] = True
        return True
    else:
        dp[i][j] = False
        return False


for _ in range(t):
    head, tail = map(int, input().strip().split())
    print(1 if recur(head - 1, tail - 1) else 0)
