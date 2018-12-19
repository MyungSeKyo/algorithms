"""
이항 쇼다운 실패
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	4253	900	749	23.075%
문제
n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 231-1 을 넘지 않는 두 자연수 n(n ≥ 1)과 k(0 ≤ k ≤n)로 이루어져 있다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 정답을 출력한다. 항상 정답이 231보다 작은 경우만 입력으로 주어진다.

예제 입력 1
4 2
10 5
49 6
0 0
예제 출력 1
6
252
13983816
"""
while True:
    n, k = map(int, input().split())

    if n == 0 and k == 0:
        break

    k = max(k, n - k)

    combination = 1
    divider = list(range(2, n - k + 1))

    for i in range(k + 1, n + 1):
        combination *= i
        while len(divider) > 0 and combination % divider[0] == 0:
            combination //= divider[0]
            divider.pop(0)
    print(combination)
