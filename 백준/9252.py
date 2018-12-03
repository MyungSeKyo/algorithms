"""
LCS 2 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	6120	2367	1876	40.738%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1
ACAYKP
CAPCAK
예제 출력 1
4
ACAK
"""
first, second = input(), input()
first_len = len(first) + 1
second_len = len(second) + 1

dp = [[0] * second_len for _ in range(first_len)]

for i in range(1, first_len):

    for j in range(1, second_len):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
path = []

i = first_len - 1
j = second_len - 1
while True:
    if dp[i][j] == dp[i][j - 1]:
        j = j - 1
    elif dp[i][j] == dp[i - 1][j]:
        i = i - 1
    else:
        i = i - 1
        j = j - 1
        path.append(first[i])

    if i == 0 or j == 0:
        break

print(''.join(reversed(path)))
