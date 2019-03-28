"""
소용돌이 예쁘게 출력하기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	3827	1032	803	31.967%
문제
크기가 무한인 정사각형 모눈종이가 있다. 모눈종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.

이 모눈종이 전체를 양의 정수의 소용돌이 모양으로 채울 것이다. 일단 숫자 1을 0행 0열에 쓴다. 그리고 나서 0행 1열에 숫자 2를 쓴다.
거기서 부터 소용돌이는 반시계 방향으로 시작된다. 다음 숫자는 다음과 같이 채우면 된다.

    -3 -2 -1  0  1  2  3
    --------------------
-3 |37 36 35 34 33 32 31
-2 |38 17 16 15 14 13 30
-1 |39 18  5  4  3 12 29
 0 |40 19  6  1  2 11 28
 1 |41 20  7  8  9 10 27
 2 |42 21 22 23 24 25 26
 3 |43 44 45 46 47 48 49
이 문제는 위와 같이 채운 것을 예쁘게 출력하면 된다. r1, c1, r2, c2가 입력으로 주어진다.
r1, c1은 가장 왼쪽 위 칸이고, r2, c2는 가장 오른쪽 아래 칸이다.

예쁘게 출력한다는 것은 다음과 같이 출력하는 것이다.

출력은 r1행부터 r2행까지 차례대로 출력한다.
각 원소는 공백으로 구분한다.
모든 행은 같은 길이를 가져야 한다.
공백의 길이는 최소로 해야 한다.
모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 한다.
만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.
입력
첫째 줄에 r1, c1, r2, c2가 주어진다. 모두 절댓값이 5000보다 작거나 같은 정수이고, r2-r1은 0보다 크거나 같고,
49보다 작거나 같으며, c2-c1은 0보다 크거나 같고, 4보다 작거나 같다.

출력
r2-r1+1개의 줄에 소용돌이를 예쁘게 출력한다.

예제 입력 1
-3 -3 2 0
예제 출력 1
37 36 35 34
38 17 16 15
39 18  5  4
40 19  6  1
41 20  7  8
42 21 22 23
"""
top, left, bottom, right = map(int, input().split())

matrix = []
max_length = 1
for y in range(top, bottom + 1):
    row = []
    for x in range(left, right + 1):
        circle_num = max(abs(y), abs(x))
        circle_size = circle_num * 2 + 1
        stacked_position = (2 * (circle_num - 1) + 1) ** 2

        if circle_num == 0:
            row.append('1')
            continue

        position = stacked_position
        if x == circle_num:
            if y == circle_num:
                position += (circle_size - 1) * 4
            else:
                position += circle_num - y
        elif y == -circle_num:
            position += circle_size - 1 + circle_num - x
        elif x == -circle_num:
            position += circle_size * 2 - 2 + circle_num + y
        elif y == circle_num:
            position += circle_size * 3 - 3 + circle_num + x

        str_position = str(position)
        if max_length < len(str_position):
            max_length = len(str_position)
        row.append(str_position)
    matrix.append(row)

for row in matrix:
    for num in row:
        num = ' ' * (max_length - len(num)) + num
        print(num, end=' ')
    print()
