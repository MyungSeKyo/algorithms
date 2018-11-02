"""
DFS와 BFS
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	49061	15318	9087	29.466%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4
"""


def dfs(edge_matrix, check_node, start_node):
    print(start_node, end=' ')
    check_node[start_node - 1] = True
    for idx, val in enumerate(edge_matrix[start_node - 1]):
        if val and not check_node[idx]:
            dfs(edge_matrix, check_node, idx + 1)


def bfs(edge_matrix, check_node, start_node):
    que = [start_node]
    check_node[start_node - 1] = True
    while que:
        current = que.pop(0)
        print(current, end=' ')
        for idx, val in enumerate(edge_matrix[current - 1]):
            if not check_node[idx] and val:
                que.append(idx + 1)
                check_node[idx] = True


node_num, edge_num, start_node = map(int, input().split())
edge_matrix = [[False] * node_num for _ in range(node_num)]

for _ in range(edge_num):
    x, y = map(int, input().split())
    edge_matrix[x - 1][y - 1] = True
    edge_matrix[y - 1][x - 1] = True
dfs(edge_matrix, [False] * len(edge_matrix), start_node)
print()
bfs(edge_matrix, [False] * len(edge_matrix), start_node)
