import sys

input = sys.stdin.readline

n = input().strip()
digits = len(n) - 1
n = int(n)

ret = 0
for i in range(digits):
    ret += 9 * (10 ** i) * (i + 1)

ret += (n - (10 ** digits - 1)) * (digits + 1)
print(ret)




MAX = '100000000' # 9자리
sum_lst = [0]
len_all = 0
for i in range(1, len(MAX)+1) :
    len_all += 9*i*10**(i-1)
    sum_lst.append(len_all)


## 원래수 - 그자리수 최소값 + 1 로 계산
n = input()

diff = int(n) - 10**(len(n)-1) + 1
diff_len = diff*len(n)

aws = diff_len + sum_lst[len(n)-1]

print(aws)