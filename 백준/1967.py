import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

tree = {i: {} for i in range(1, n + 1)}

for _ in range(n - 1):
    mother, child, cost = map(int, input().strip().split())

    tree[mother][child] = cost


maxi = 0

def recur(node):
    if not tree[node]:
        return 0

    legs = [0, 0]

    for child in tree[node]:
        legs.append(recur(child) + tree[node][child])

    legs = sorted(legs, reverse=True)

    global maxi
    maxi = max(sum(legs[:2]), maxi)

    return max(legs)

recur(1)
print(maxi)

