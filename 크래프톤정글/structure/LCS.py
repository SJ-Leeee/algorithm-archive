def lcs_recur(x, y):
    m, n = len(x), len(y)

    if m == 0 or n == 0:
        return 0

    else:
        if x[-1] == y[-1]:
            return lcs_recur(x[: (m - 1)], y[: (n - 1)]) + 1
        else:
            return max(
                lcs_recur(x[: (m - 1)], y),
                lcs_recur(x, y[: (n - 1)]),
            )


"""
중복 부분 문제 발견 O(2^n)
"""

# memo = {}


# def lcs_recur_with_memo(x, y):
#     m, n = len(x), len(y)

#     if m == 0 or n == 0:
#         return 0

#     else:
#         if x[-1] == y[-1]:
#             if (m - 1, n - 1) in memo:
#                 return memo[(m - 1, n - 1)]
#             else:
#                 memo[(m - 1, n - 1)] = lcs_recur(x[: (m - 1)], y[: (n - 1)]) + 1
#                 return memo[(m - 1, n - 1)]
#         else:
#             if (m, n - 1) not in memo:
#                 memo[(m, n - 1)] = lcs_recur(x, y[: (n - 1)])
#             if (m - 1, n) not in memo:
#                 memo[(m - 1, n)] = lcs_recur(x, y[: (n - 1)])
#             return max(memo[(m, n - 1)], memo[(m - 1, n)])


def lcs_topdown_with_dp(x, y, memo=None):
    """메모화 버전"""
    if memo is None:
        memo = {}

    m, n = len(x), len(y)

    # 이미 계산된 결과가 있으면 반환
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        result = 0
    else:
        if x[-1] == y[-1]:
            result = lcs_topdown_with_dp(x[: (m - 1)], y[: (n - 1)], memo) + 1
        else:
            result = max(
                lcs_topdown_with_dp(x[: (m - 1)], y, memo),
                lcs_topdown_with_dp(x, y[: (n - 1)], memo),
            )

    memo[(m, n)] = result
    return result


# if __name__ == "__main__":
#     x = "ABCDGH"
#     y = "AEDFHR"

#     print(f"기본 재귀: {lcs_recur(x, y)}")
#     print(f"메모화: {lcs_recur_with_memo(x, y)}")

#     # 더 긴 문자열로 성능 차이 확인
#     x_long = "ABCDEFGHIJKLMNOP"
#     y_long = "ACEGIKMOQSUWY"

#     import time

#     # 메모화 버전만 테스트 (기본 재귀는 너무 오래 걸림)
#     start = time.time()
#     result = lcs_recur_with_memo(x_long, y_long)
#     end = time.time()

#     start2 = time.time()
#     result2 = lcs_recur(x_long, y_long)
#     end2 = time.time()

#     print(f"긴 문자열 LCS: {result}, 시간: {end - start:.4f}초")
#     print(f"긴 문자열 LCS: {result2}, 시간: {end2 - start2:.4f}초")


def lcs_bottomup(x, y):
    x, y = [""] + x, [""] + y  # 인덱스 추가
    m, n = len(x), len(y)

    c = [[0 for _ in range(n)] for _ in range(m)]
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
                b[i][j] = (
                    2 if c[i - 1][j] > c[i][j - 1] else 3
                )  # 위에서 왔으면 2, 왼쪽에서 왔으면 3
    return c, b


def get_lcs(m, n, b, x):
    if m == 0 or n == 0:
        return ""
    else:
        if b[m][n] == 1:
            print(x[m], m)
            return get_lcs(m - 1, n - 1, b, x) + x[m]
        elif b[m][n] == 2:
            return get_lcs(m - 1, n, b, x)
        elif b[m][n] == 3:
            return get_lcs(m, n - 1, b, x)


x = list("ACAYKP")
y = list("CAPCAK")
m = len(x)
n = len(y)
c, b = lcs_bottomup(x, y)
for i in b:
    print(i)
print(get_lcs(m, n, b, [""] + x))
