"""
단어 정렬
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	15545	5524	3992	36.410%
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.


출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.


예제 입력 1
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
예제 출력 1
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""
import sys

list_per_length = {}
word_num = int(input())

for _ in range(word_num):
    word = input()
    if list_per_length.get(len(word)):
        list_per_length[len(word)].append(word)
    else:
        list_per_length[len(word)] = [word]

lengths = list_per_length.keys()
for length in lengths:
    list_per_length[length] = sorted(list(set(list_per_length[length])))

lengths = sorted(lengths)

for length in lengths:
    for word in list_per_length[length]:
        print(word)
