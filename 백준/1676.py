"""
팩토리얼 0의 개수
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	8973	3903	3308	46.227%
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1
10
예제 출력 1
2
"""
n = int(input())

ret = 1
for i in range(1, n + 1):
    ret *= i

ret = reversed(str(ret))

count = 0
for digit in ret:
    if digit == '0':
        count += 1
    else:
        break

print(count)