"""
평범한 배낭
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	1028	360	245	35.252%
문제
이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다.
세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에,
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데,
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
아직 행군을 해본 적이 없는 준서는 최대 K무게까지의 배낭만 들고 다닐 수 있다.
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

예제 입력 1
4 7
6 13
4 8
3 6
5 12
예제 출력 1
14

"""
item_num, max_weight = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(item_num)]
items = sorted(items, key=lambda x: x[0])
weights = list(map(lambda x: x[0], items))
values = list(map(lambda x: x[1], items))

max_weight += 1
dp = [[0] * max_weight for _ in range(item_num)]

for i in range(item_num):
    for j in range(max_weight):
        if j - weights[i] >= 0:
            dp[i][j] = max(dp[i - 1][j - weights[i]] + values[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
