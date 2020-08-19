import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().strip().split()))

head, tail = 0, 0
total = arr[0]
ret = 0


while True:
    if total < m:
        tail += 1
        if tail < n:
            total += arr[tail]
        else:
            break
    elif total == m:
        ret += 1
        tail += 1
        if tail < n:
            total += arr[tail]
        else:
            break
    elif total > m:
        total -= arr[head]
        head += 1

print(ret)
