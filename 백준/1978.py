"""
소수 찾기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	20477	9899	8272	50.476%
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
예제 출력 1
3
"""
MAX_NUM = 1000
sosoo_list = [True] * MAX_NUM


for i in range(1, MAX_NUM):
    if sosoo_list[i]:
        multipled = (i + 1) * 2
        while multipled <= MAX_NUM:
            sosoo_list[multipled - 1] = False
            multipled = multipled + i + 1

input()
nums = map(int, input().split())
count = 0
for num in nums:
    if sosoo_list[num - 1] and num != 1:
        count += 1

print(count)