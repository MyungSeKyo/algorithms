import sys
import itertools
input = sys.stdin.readline

n = int(input())

arr = list(input().strip().split())

mini = 10000000000
maxi = 0
for nums in itertools.permutations(range(10), n + 1):
    ret = True
    for i in range(n):
        if arr[i] == '<':
            if nums[i] < nums[i + 1]:
                pass
            else:
                ret = False
                break
        else:
            if nums[i] > nums[i + 1]:
                pass
            else:
                ret = False
                break
    if ret:
        mini = min(mini, int(''.join(map(str, nums))))
        maxi = max(maxi, int(''.join(map(str, nums))))

print(str(maxi).zfill(n + 1))
print(str(mini).zfill(n + 1))
