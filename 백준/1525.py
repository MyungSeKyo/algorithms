import sys
import collections
import copy
input = sys.stdin.readline

init_board = []
for _ in range(3):
    init_board += list(input().strip().split())
visit = set()
visit.add(''.join(init_board))

queue = collections.deque([(''.join(init_board), init_board.index('0'), 0)])

cases = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [7, 5],
}

def sol():
    while len(queue) > 0:
        board_str, zero_index, depth = queue.popleft()

        for i in cases[zero_index]:
            board = list(board_str)
            board[i], board[zero_index] = board[zero_index], board[i]
            new_board_str = ''.join(board)
            if new_board_str == '123456780':
                return depth + 1

            if new_board_str not in visit:
                visit.add(new_board_str)
                queue.append((new_board_str, i, depth + 1))
    return -1


if ''.join(init_board) == '123456780':
    print(0)
else:
    print(sol())
