import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visit = set()
    visit.add(a)
    queue = collections.deque([(a, '')])

    ret = 'No'
    while len(queue) > 0:
        a, depth = queue.popleft()

        new_a = (a * 2) % 10000
        if new_a not in visit:
            visit.add(new_a)
            queue.append((new_a, depth + 'D'))
            if new_a == b:
                ret = depth + 'D'
                break

        new_a = 9999 if a == 0 else a - 1
        if new_a not in visit:
            visit.add(new_a)
            queue.append((new_a, depth + 'S'))
            if new_a == b:
                ret = depth + 'S'
                break

        new_a = str(a).zfill(4)
        new_a = new_a[1:] + new_a[0]
        new_a = int(new_a)
        if new_a not in visit:
            visit.add(new_a)
            queue.append((new_a, depth + 'L'))
            if new_a == b:
                ret = depth + 'L'
                break

        new_a = str(a).zfill(4)
        new_a = new_a[-1] + new_a[:-1]
        new_a = int(new_a)
        if new_a not in visit:
            visit.add(new_a)
            queue.append((new_a, depth + 'R'))
            if new_a == b:
                ret = depth + 'R'
                break
    print(ret)
