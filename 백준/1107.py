import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

buttons = [str(i) for i in range(10)]

for not_work in input().split():
    buttons.remove(not_work)

diff = abs(100 - n)
str_diff = ''

def bfs(str_num):
    global diff, str_diff
    if str_num:
        ret = abs(n - int(str_num))
        if diff > ret + len(str_num):
            diff = ret + len(str_num)
            str_diff = str_num

    if len(str_num) < 6 and str_num != '0':
        for btn in buttons:
            bfs(str_num + btn)

bfs('')

print(diff)
