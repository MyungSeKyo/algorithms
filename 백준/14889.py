import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
all = set(range(n))

ret = 10000000000
for a in combinations(all, n // 2):
    b = list(all - set(a))

    a_sum = 0
    for a1 in a:
        for a2 in a:
            a_sum += costs[a1][a2]

    b_sum = 0
    for b1 in b:
        for b2 in b:
            b_sum += costs[b1][b2]

    ret = min(abs(a_sum - b_sum), ret)

print(ret)
