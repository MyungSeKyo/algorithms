import sys
import math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
remain = tuple(map(int, input().strip().split()))

if n == 1:
    print(math.ceil(remain[0] / 9))
    exit()

dp = {}

case3 = [
    (9, 3, 1),
    (9, 1, 3),
    (3, 9, 1),
    (3, 1, 9),
    (1, 9, 3),
    (1, 3, 9),
]
case2 = [
    (9, 3),
    (3, 9),
]


def recur(current):
    if current in dp:
        return dp[current]

    complete = True
    for i in range(n):
        if current[i] < remain[i]:
            complete = False

    if complete:
        return 0

    if n == 3:
        case = case3
    else:
        case = case2

    mini = 1000000
    for cas in case:
        new_current = tuple()
        for i in range(n):
            new_current += (current[i] + cas[i], )
        mini = min(recur(new_current), mini)

    dp[current] = mini + 1
    return mini + 1

recur((0 ,) * n)
print(dp[(0,) * n])