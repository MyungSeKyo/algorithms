"""
베르트랑 공준
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	7380	3376	2838	50.679%
문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)

입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

예제 입력 1
1
10
13
100
1000
10000
100000
0
예제 출력 1
1
4
3
21
135
1033
8392
"""
MAX_NUM = 123456 * 2
sosoo_list = [True] * MAX_NUM


for i in range(1, MAX_NUM):
    if sosoo_list[i]:
        multipled = (i + 1) * 2
        while multipled <= MAX_NUM:
            sosoo_list[multipled - 1] = False
            multipled = multipled + i + 1
sosoo_list[0] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        count = 0
        for i in range(n, 2 * n):
            if sosoo_list[i]:
                count += 1
        print(count)
