import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().strip().split()))

head, tail = 0, 0
total = arr[0]
length = 1
ret = None

while True:
    if total >= m:
        if ret is None:
            ret = length
        else:
            ret = min(ret, length)
        total -= arr[head]
        head += 1
        length -= 1
    else:
        length += 1
        tail += 1
        if tail < n:
            total += arr[tail]
        else:
            break

print(ret if ret is not None else 0)
