"""
이항 계수 3
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	3248	1313	979	50.051%
문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )

출력
 를 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1
5 2
예제 출력 1
10
"""
n, k = map(int, input().split())
p = 1000000007

k_factor = 1
n_factor = 1
n_k_factor = 1
n_k = n - k


def recur_power(a, b):
    if b == 0:
        return 1
    else:
        sub = recur_power(a, b // 2)
        sub *= sub
        if b % 2 == 1:
            sub *= a
        return sub % p


def loop_power(a, b):
    extra = 1

    if b == 0:
        return 1

    while b > 1:
        if b % 2 == 1:
            extra *= a
            extra %= p
        b //= 2
        a *= a
        a %= p
    return (a * extra) % p


for i in range(2, n + 1):
    if i <= k:
        k_factor *= i
        k_factor %= p
    if i <= n_k:
        n_k_factor *= i
        n_k_factor %= p
    n_factor *= i
    n_factor %= p
#
print(n_factor * loop_power(n_k_factor * k_factor % p, p - 2) % p)
