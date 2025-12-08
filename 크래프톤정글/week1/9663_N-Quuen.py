# import copy
# import time

# N = int(input())

# def n_queen(queen, visited, result, depth, N):
#     global count
#     if depth == N:
#         count += 1

#     for i in range(N):
#         if is_possible(i, depth, N):  # 여기서 열검사 하는데?
#             return

#         if not visited[i]:  # 같은컬럼에 있으면 안되므로
#             visited[i] = True


# def is_possible(col, row, N):
#     for i in range(N):
#         if queen[i] == col:
#             return False

#     k = 1
#     while True:
#         new_row = row + k
#         new_col = col + k

#         queen[new_row] == new_col

#         if not (0 <= new_row < N and 0 <= new_col < N):
#             break

#         k += 1


# def n_queen_bool_switch(board, row, col, N, b_swt, prev_board):
#     for i in range(N):
#         if board[row][i] == False:
#             prev_board.append((row, i))
#         board[row][i] = b_swt

#     # 세로 전부 사용
#     for j in range(N):
#         if board[j][col] == False:
#             prev_board.append((j, col))
#         board[j][col] = b_swt

#     # 대각선
#     diagonal = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
#     for dr, dc in diagonal:
#         k = 1
#         while True:
#             new_row = row + dr * k
#             new_col = col + dc * k

#             if not (0 <= new_row < N and 0 <= new_col < N):
#                 break

#             if board[new_row][new_col] == False:
#                 prev_board.append((new_row, new_col))
#             board[new_row][new_col] = b_swt
#             k += 1


# def restore_board(board, prev_board):
#     for row, col in prev_board:
#         board[row][col] = False


# start1 = time.time()

# a = n_queen(board, result, 0, N)
# print(a)
# end1 = time.time()
# print(f"Nqueen!!{end1- start1} 초")
# for i in range(row, N):
#     for j in range(col, N):
#         if not board[i][j]:
#             board[i][j] = True
#             result[i][j] = 1
#             n_queen_bool_switch(board, row, col, N, True)
#             n_queen(board, row + 1, col + 1, depth + 1, N, count)
#             n_queen_bool_switch(board, row, col, N, False)
#             result[i][j] = 0
#             board[i][j] = False

# for i in range(N):
#     if not board[depth][i]:
#         board[depth][i] = True
#         result[depth][i] = 1
#         prev_board = copy.deepcopy(board)
#         n_queen_bool_switch(board, depth, i, N, True)
#         n_queen(board, result, depth + 1, N, count)
#         for i in range(N):
#             for j in range(N):
#                 board[i][j] = prev_board[i][j]
#         result[depth][i] = 0
#         board[depth][i] = False


import time


N = int(input())
queen = [[False for _ in range(N)] for _ in range(N)]

count = 0


def n_queen(queen, depth, N):
    global count
    if depth == N:
        count += 1
        return

    for i in range(N):
        if is_possible(queen, depth, i, N):
            queen[depth][i] = True
            n_queen(queen, depth + 1, N)
            queen[depth][i] = False


def is_possible(queen, depth, col, N):
    for row in range(depth):
        if queen[row][col]:
            return False

    for i in range(depth):
        for j in range(N):
            if queen[i][j]:
                if abs(i - depth) == abs(j - col):
                    return False
                break

    return True


n_queen(queen, 0, N)
print(count)
# start1 = time.time()
# n_queen(queen, 0, N)
# print(count)
# end1 = time.time()
# print(f"Nqueen!!{end1- start1:.5f} 초")
