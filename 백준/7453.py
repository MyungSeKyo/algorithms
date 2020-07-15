import sys

input = sys.stdin.readline

n = int(input())
arr1, arr2, arr3, arr4 = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr1.append(a)
    arr2.append(b)
    arr3.append(c)
    arr4.append(d)

arr12 = {}
for i in range(n):
    for j in range(n):
        num = arr1[i] + arr2[j]
        if num in arr12:
            arr12[num] += 1
        else:
            arr12[num] = 1

arr34 = {}
for i in range(n):
    for j in range(n):
        num = arr3[i] + arr4[j]
        if num in arr34:
            arr34[num] += 1
        else:
            arr34[num] = 1

ret = 0
for a in arr12:
    if -a in arr34:
        ret += arr12[a] * arr34[-a]

print(ret)