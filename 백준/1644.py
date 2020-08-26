import sys
input = sys.stdin.readline

n = int(input())

che = [True] * (n + 1)

for i in range(2, n + 1):
    if che[i]:
        for j in range(2 * i, n + 1, i):
            che[j] = False

primes = [i for i in range(2, n + 1) if che[i]]

if primes:
    head = 0
    tail = 0
    total = primes[0]
    ret = 0
    while True:
        if total == n:
            ret += 1

            tail += 1
            if tail < len(primes):
                total += primes[tail]
            else:
                break

        elif total < n:
            tail += 1
            if tail < len(primes):
                total += primes[tail]
            else:
                break
        else:
            total -= primes[head]
            head += 1
            if head >= len(primes):
                break

    print(ret)
else:
    print(0)
