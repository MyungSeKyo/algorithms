import sys
import itertools
input = sys.stdin.readline

n = int(input())

alpha = {}
for _ in range(n):
    word = reversed(input().strip())

    for i, val in enumerate(word):
        if val in alpha:
            alpha[val] += 10 ** i
        else:
            alpha[val] = 10 ** i
alpha = sorted(alpha.values(), reverse=True)

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

ret = 0
for i in range(len(alpha)):
    ret += alpha[i] * nums[i]

print(ret)