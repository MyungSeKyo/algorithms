"""
문제
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""


def is_hansoo(num):
    nums = list(map(int, str(num)))
    idx = 0

    while idx < len(nums) - 2:
        if nums[idx] - nums[idx + 1] != nums[idx + 1] - nums[idx + 2]:
            return False
        idx = idx + 1
    return True


max = int(input())

i = 0
count = 0
while i < max:
    if is_hansoo(i + 1):
        count = count + 1
    i = i + 1

print(count)
