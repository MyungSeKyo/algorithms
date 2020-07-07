import sys
import collections

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    if v == 1:
        print('NO')
        continue
    visit = [None] * (v + 1)
    graph = {i: set() for i in range(1, v + 1)}
    for _ in range(e):
        from_node, to_node = map(int, input().split())

        if from_node in graph:
            graph[from_node].add(to_node)
        if to_node in graph:
            graph[to_node].add(from_node)

    ret = 'YES'
    for current in range(1, v + 1):
        if visit[current] is None:
            que = collections.deque([(current, 1)])
            visit[current] = 1

            while len(que) > 0:
                node, color = que.popleft()

                for n in graph[node]:
                    if visit[n] is None:
                        visit[n] = -color
                        que.append((n, -color))
                    elif visit[n] is color:
                        ret = 'NO'
                        break
                    elif visit[n] is -color:
                        continue
            if ret == 'NO':
                break
    # print(visit)
    print(ret)
