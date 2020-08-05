import sys
import collections
input = sys.stdin.readline

a, b = map(int, input().split())
if a != b:
    queue = collections.deque([(a, 0)])
    visit = set()

    total_depth = None
    ret_count = 0
    while len(queue) > 0:
        n, depth = queue.popleft()
        visit.add(n)
        cases = [n * 2, n + 1, n - 1]

        for case in cases:
            if case not in visit and 0 <= case < 200000:
                if case == b:
                    if total_depth is None:
                        total_depth = depth + 1
                        ret_count += 1
                    else:
                        if total_depth == depth + 1:
                            ret_count += 1
                else:
                    queue.append((case, depth + 1))

    print(total_depth)
    print(ret_count)
else:
    print(0)
    print(1)
