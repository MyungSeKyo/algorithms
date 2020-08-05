import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

memo = {

}


def recur(w, h):
    if (w, h) in memo:
        return memo[(w, h)]

    if w == 0:
        return 1

    if h == 0:
        return recur(w - 1, h + 1)
    memo[(w, h)] = recur(w - 1, h + 1) + recur(w, h - 1)

    return memo[(w, h)]

n = int(input())

while n != 0:
    print(recur(n, 0))
    n = int(input())