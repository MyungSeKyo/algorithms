//검문
//시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
//1 초	128 MB	5258	919	735	21.561%
//문제
//트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다.
//경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에,
//검문하는데 엄청나게 오랜 시간이 걸린다.
//
//상근이는 시간을 때우기 위해서 수학 게임을 하기로 했다.
//
//먼저 근처에 보이는 숫자 N개를 종이에 적는다.
//그 다음, 종이에 적은 수를 M으로 나누었을 때,
//나머지가 모두 같게 되는 M을 모두 찾으려고 한다. M은 1보다 커야 한다.
//
//N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.
//
//입력
//첫째 줄에 종이에 적은 수의 개수 N이 주어진다. (2 ≤ N ≤ 100)
//
//다음 줄부터 N개 줄에는 종이에 적은 수가 하나씩 주어진다.
//이 수는 모두 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다. 같은 수가 두 번 이상 주어지지 않는다.
//
//항상 M이 하나 이상 존재하는 경우만 입력으로 주어진다.
//
//출력
//첫째 줄에 가능한 M을 공백으로 구분하여 모두 출력한다. 이때, M은 증가하는 순서이어야 한다.
//
//예제 입력 1
//3
//6
//34
//38
//예제 출력 1
//2 4
#include<stdio.h>
#include <math.h>

int gcd(int a, int b){
    int temp = 0;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main(){
    int number_of_nums = 0;
    int before = 0;
    int current = 0;
    int total_gcd = 0;

    scanf("%d", &number_of_nums);
    scanf("%d", &before);
    scanf("%d", &current);

    total_gcd = abs(current - before);

    before = current;

    for (int i = 2; i < number_of_nums; i++) {
        scanf("%d", &current);
        total_gcd = gcd(total_gcd, abs(current - before));
        before = current;
    }

    for (int i = 2; i <= total_gcd / 2; i++) {
        if (total_gcd % i == 0) {
            printf("%d ", i);
        }
    }
    printf("%d", total_gcd);
}