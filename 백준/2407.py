"""
조합
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	7393	1708	1466	31.939%
문제
nCm을 출력한다.

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.

예제 입력 1
100 6
예제 출력 1
1192052400
"""
n, m = map(int, input().split())
ret = 1

for i in range(n - m + 1, n + 1):
    ret *= i

for i in range(1, m + 1):
    ret //= i

print(ret)
