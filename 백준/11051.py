"""
이항 계수 1
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	7371	4632	4000	64.819%
문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 를 출력한다.

예제 입력 1
5 2
예제 출력 1
10
"""
n, k = map(int, input().split())

k = min(n - k, k)

result = 1

for num in range(n - k + 1, n + 1):
    result *= num

for num in range(1, k + 1):
    result //= num

print(result)
