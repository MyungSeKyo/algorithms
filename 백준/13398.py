import sys
input = sys.stdin.readline
MAX = 1000000
n = int(input())
arr = list(map(int, input().split()))

total = 0
maxi = 0
total1 = 0
total2 = 0
for i in range(n):
    temp = total1
    total1 = max(total1 + arr[i], arr[i])
    total2 = max(temp, total2 + arr[i], arr[i])
    maxi = max(total1, maxi)
    maxi = max(total2, maxi)

if maxi == 0:
    print(max(arr))
else:
    print(maxi)
