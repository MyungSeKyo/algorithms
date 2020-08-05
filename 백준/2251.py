import sys
import collections
input = sys.stdin.readline

a, b, c = map(int, input().split())
visit = {(a, b, c)}
queue = collections.deque([(0, 0, c)])
answer = {c}

while len(queue) > 0:
    aa, bb, cc = queue.popleft()

    # a -> c
    if aa and cc < c:
        remain = c - cc
        if aa >= remain:
            ret = (aa - remain, bb, c)
        else:
            ret = (0, bb, cc + aa)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

    # c -> a
    if cc and aa < a:
        remain = a - aa
        if cc >= remain:
            ret = (a, bb, cc - remain)
        else:
            ret = (aa + cc, bb, 0)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

    # a -> b
    if aa and bb < b:
        remain = b - bb
        if aa >= remain:
            ret = (aa - remain, b, cc)
        else:
            ret = (0, bb + aa, cc)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

    # b -> a
    if bb and aa < a:
        remain = a - aa
        if bb >= remain:
            ret = (a, bb - remain, cc)
        else:
            ret = (aa + bb, 0, cc)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

    # b -> c
    if bb and cc < c:
        remain = c - cc
        if bb >= remain:
            ret = (aa, bb - remain, c)
        else:
            ret = (aa, 0, cc + bb)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

    # c -> b
    if cc and bb < b:
        remain = b - bb
        if cc >= remain:
            ret = (aa, b, cc - remain)
        else:
            ret = (aa, bb + cc, 0)
        if ret not in visit:
            visit.add(ret)
            queue.append(ret)
            if ret[0] == 0:
                answer.add(ret[2])

for i in sorted(answer):
    print(i, end=' ')
