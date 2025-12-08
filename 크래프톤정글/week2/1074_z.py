"""
의사코드
N에 따라서 위치가 달라진다
N이 1까지
"""

# count = 0


# def z_print(N, x, y, row, col):
#     # 다 만들 필요가 없음
#     global count

#     if N == 1:
#         # 작업을 할건데
#         if x == row and y == col:
#             return count
#         count += 1
#         if x == row and y + 1 == col:
#             return count
#         count += 1
#         if x + 1 == row and y == col:
#             return count
#         count += 1
#         if x + 1 == row and y + 1 == col:
#             return count
#         count += 1
#         return None

#     add_x = 2 ** (N - 1)
#     add_y = 2 ** (N - 1)
#     get_count = z_print(N - 1, x, y, row, col)
#     if get_count != None:
#         return count
#     get_count = z_print(N - 1, x, y + add_y, row, col)
#     if get_count != None:
#         return count
#     get_count = z_print(N - 1, x + add_x, y, row, col)
#     if get_count != None:
#         return count
#     get_count = z_print(N - 1, x + add_x, y + add_y, row, col)
#     if get_count != None:
#         return count


# N, r, c = map(int, input().split())

# a = z_print(N, 0, 0, r, c)
# print(a)

import time


count = 0


# def z_print(N, row_locate, col_locate, row, col):
#     # 다 만들 필요가 없음
#     global count

#     if N == 1:
#         if row_locate == row and col_locate == col:
#             return count
#         count += 1
#         if row_locate == row and col_locate + 1 == col:
#             return count
#         count += 1
#         if row_locate + 1 == row and col_locate == col:
#             return count
#         count += 1
#         if row_locate + 1 == row and col_locate + 1 == col:
#             return count
#         count += 1
#         return

#     half = 2 ** (N - 1)
#     # 4 4
#     # 2 2
#     # my = 1, 2

#     one_sector = 4 ** (N - 1)

#     if col >= col_locate + half and row >= row_locate + half:
#         count += one_sector * 3
#         z_print(N - 1, row_locate + half, col_locate + half, row, col)
#     elif col >= col_locate + half:
#         count += one_sector
#         z_print(N - 1, row_locate, col_locate + half, row, col)
#     elif row >= row_locate + half:
#         count += one_sector * 2
#         z_print(N - 1, row_locate + half, col_locate, row, col)
#     else:
#         z_print(N - 1, row_locate, col_locate, row, col)

#     return
#     # row >= x + add_x
#     # 이친구는 1사분면인거야


# N, r, c = map(int, input().split())
# start = time.time()
# z_print(N, 0, 0, r, c)
# print(count)
# end = time.time()
# print(f"{end - start:.5f} sec")


def z_print(N, row_locate, col_locate, row, col):
    global count

    if N == 1:
        # 2x2 격자에서 순서대로 체크
        for dr, dc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if row_locate + dr == row and col_locate + dc == col:
                return count
            count += 1
        return

    half = 2 ** (N - 1)
    one_sector = 4 ** (N - 1)

    # 오른쪽/아래쪽 여부 확인
    is_right = col >= col_locate + half
    is_bottom = row >= row_locate + half

    # 사분면에 따른 처리
    if is_bottom and is_right:  # 4사분면
        count += one_sector * 3
        z_print(N - 1, row_locate + half, col_locate + half, row, col)
    elif is_right:  # 2사분면
        count += one_sector * 1
        z_print(N - 1, row_locate, col_locate + half, row, col)
    elif is_bottom:  # 3사분면
        count += one_sector * 2
        z_print(N - 1, row_locate + half, col_locate, row, col)
    else:  # 1사분면
        z_print(N - 1, row_locate, col_locate, row, col)
