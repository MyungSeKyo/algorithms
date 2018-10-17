"""
2007년
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	45438	18323	15844	42.477%
문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

예제 입력 1
1 1
예제 출력 1
MON
예제 입력 2
3 14
예제 출력 2
WED
예제 입력 3
9 2
예제 출력 3
SUN
예제 입력 4
12 25
예제 출력 4
TUE
"""
month, date = list(map(int, input().split()))
sum_of_day = date

for mon in range(1, month):
    if mon in (4, 6, 9, 11):
        sum_of_day = sum_of_day + 30
    elif mon == 2:
        sum_of_day = sum_of_day + 28
    else:
        sum_of_day = sum_of_day + 31

if sum_of_day % 7 == 0:
    day_name = 'SUN'
elif sum_of_day % 7 == 1:
    day_name = 'MON'
elif sum_of_day % 7 == 2:
    day_name = 'TUE'
elif sum_of_day % 7 == 3:
    day_name = 'WED'
elif sum_of_day % 7 == 4:
    day_name = 'THU'
elif sum_of_day % 7 == 5:
    day_name = 'FRI'
else:
    day_name = 'SAT'

print(day_name)
