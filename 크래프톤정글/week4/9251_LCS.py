# import sys


# def lcs(s1, s2, dp=None):
#     if not dp:
#         dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

#     s1_len = len(s1)
#     s2_len = len(s2)

#     if dp[s1_len][s2_len]:
#         return dp[s1_len][s2_len]

#     if not s1_len or not s2_len:
#         return 0

#     if s1[-1] == s2[-1]:
#         dp[s1_len][s2_len] = lcs(s1[:-1], s2[:-1], dp) + 1
#     else:
#         dp[s1_len][s2_len] = max(lcs(s1[:-1], s2, dp), lcs(s1, s2[:-1], dp))

#     return dp[s1_len][s2_len]


# s1 = ["A", "B", "C", "D"]
# s2 = ["B", "C", "A", "3", "D"]

# print(lcs(s1, s2))


import sys


def lcs_btu(s1, s2):
    s1 = [""] + s1
    s2 = [""] + s2
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    s1_len = len(s1)
    s2_len = len(s2)

    for i in range(1, s1_len):
        for j in range(1, s2_len):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[s1_len - 1][s2_len - 1]


s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

print(lcs_btu(s1, s2))
