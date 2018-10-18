"""
그룹 단어 체커
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	12015	5902	5214	50.720%
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1
3
happy
new
year
예제 출력 1
3
예제 입력 2
4
aba
abab
abcabc
a
예제 출력 2
1
"""
input()
total = 0
while True:
    try:
        word = input()
        alphabets = [False] * (ord('z') - ord('a') + 1)

        is_group_num = True
        before = word[0]
        alphabets[ord(before) - ord('a')] = True
        for i in range(1, len(word)):
            if word[i] != before:
                if alphabets[ord(word[i]) - ord('a')]:
                    is_group_num = False
                    break
                else:
                    alphabets[ord(word[i]) - ord('a')] = True
            before = word[i]
        if is_group_num:
            total = total + 1
    except:
        break

print(total)
