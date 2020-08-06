a, b = map(int, input().split())

num = [True] * (b - a + 1)
count = 0
current = 2

square = current * current
while current * current <= b:
    i = a // square
    while square * i <= b:
        idx = square * i - a

        if idx >= 0 and num[idx]:
            count += 1
            num[idx] = False
        i += 1
    current += 1
    square = current * current
print(len(num) - count)
