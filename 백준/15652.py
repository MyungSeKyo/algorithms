


import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

queue = collections.deque()

for i in range(1, n + 1):
    queue.append((i, [i]))


while len(queue) > 0:
    current, before = queue.popleft()
    if len(before) >= m:
        print(' '.join(map(str, before)))
    else:
        for i in range(current, n + 1):
            queue.append((i, before + [i]))
