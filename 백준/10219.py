"""
Meats On The Grill 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	2035	1185	1039	61.845%
문제
Coders High 2014가 끝났다. 저녁 회식은 취소되었기 때문에 참가자들은 뿔뿔이 흩어져 저녁식사를 하기 위해 떠났다.
사람들이 모여서 먹는 저녁식사 중에서도 가장 대중적인 것은 고기! Coders High의 출제진들도 고깃집에 와서 고기를 시켰다.
명우는 고기를 구워야 하는 중책을 맡게 되었으므로 불판 위에 고기들을 얹었다.
뛰어난 문제 해결 능력을 가진 명우는 불판 위의 고기를 다음과 같이 모델링하기로 했다.

편의상 불판을  H × W개의 칸으로 이루어진 격자로 나타내기로 하고, 고기는 격자의 여러 칸 위에 걸쳐 있는 것으로 표현한다.
또한 고기가 격자 위에 올라와 있으면, 격자를 가득 채우게 된다고 생각한다.

 시간이 지나 현재 아래쪽 면은 적당히 구워졌기 때문에 고기를 뒤집을 시간이 되었다.



같은 덩이에 속하는 고기는 뒤집을 경우 모두 같이 뒤집히게 된다. 첫 번째 그림이 원래 고기가 불판 위에 있었던 상태라고 하자.
두 번째 그림은 고기를 좌우 대칭으로 뒤집은 그림이라고 할 수 있다. 세 번째 그림은 고기를 뒤집었지만,
고기가 불판의 격자 칸 위에 제대로 위치하고 있지 않다. 명우는 이런 경우를 끔찍히 싫어하기 때문에 저렇게 뒤집지 않을 것이다.
네 번째 그림은 뒤집은 후 오른쪽으로 90˚돌려진 형태인데, 이런 형태도 가능하며, 180˚, 270˚로 돌리는 것도 가능하다.

명우는 고기가 불판 위에 올려진 상태가 주어질 때, 한 덩이에 속하는 고기 각각이 뒤집힌 상태가 되도록 만들고 싶다.
명우는 완벽주의자이기 때문에 모든 고기를 뒤집은 후에 고기가 겹쳐져 있는 경우가 생기는 것을 끔찍히 싫어한다.
명우에게 어떻게 뒤집어야 고기를 겹치지 않게 뒤집을 수 있는지 알려주자!

입력
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 격자의 크기를 의미하는 두 정수 H, W (1 ≤ H, W ≤ 11)가 공백으로 구분되어 주어진다.

다음 H개의 줄에 현재 불판의 상태가 주어지는데, 각 줄에는 W개의 문자가 공백 없이 주어져 있다.
문자는 알파벳 소문자 혹은 '.'으로 주어지며, 알파벳 소문자가 같은 경우에는 같은 덩이에 속하는 고기라는 것을 의미한다.
같은 덩이에 속한다는 것은 이 격자들만을 이용하여 상하좌우로 움직이는 것으로 다른 모든 같은 덩이의 격자를 방문 가능하다는 것을 의미한다.

출력
각 테스트 케이스마다 각 고기덩이를 뒤집은 후의 불판의 상태를 H줄에 걸쳐서 출력한다. 각 줄에는 W개의 문자가 있어야 하며,
입력에서 주어진 각 고기 덩이가 뒤집힌 채로 있어야 한다. 이를 만족하는 어느 답을 출력해도 정답으로 인정한다.

예제 입력 1
1
3 4
abbb
aabb
aa..
예제 출력 1
.abb
aabb
aa.b
"""
test_num = int(input())

for _ in range(test_num):
    width, height = map(int, input().split())
    for _ in range(width):
        row = input()
        print(row[::-1])
