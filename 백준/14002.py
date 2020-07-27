import sys
import collections
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp_arr = [[] for _ in range(n)]


for i in range(n):
    maxi = []
    for j in range(i):
        if arr[j] < arr[i]:
            maxi = max(maxi, dp_arr[j], key=lambda x: len(x))
    dp_arr[i] = maxi + [arr[i]]

maxi = max(dp_arr, key=lambda x: len(x))
print(len(maxi))
print(' '.join(map(lambda x: str(x), maxi)))
