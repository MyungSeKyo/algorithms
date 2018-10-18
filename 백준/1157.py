"""
단어 공부
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	26584	9227	7276	35.317%
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1
Mississipi
예제 출력 1
?
예제 입력 2
zZa
예제 출력 2
Z
예제 입력 3
z
예제 출력 3
Z
예제 입력 4
baaa
예제 출력 4
A
"""
word = input().upper()
alphabets = [0] * (ord('Z') - ord('A') + 1)

for char in word:
    alphabets[ord(char) - ord('A')] = alphabets[ord(char) - ord('A')] + 1

max = 0
max_char = '????'
duplicated_max = False

for idx, num in enumerate(alphabets):
    if num > max:
        max = num
        max_char = chr(idx + ord('A'))
        duplicated_max = False
    elif num == max:
        duplicated_max = True

if duplicated_max:
    print('?')
else:
    print(max_char)
