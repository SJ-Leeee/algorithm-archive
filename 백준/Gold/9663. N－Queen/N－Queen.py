import sys
input = sys.stdin.readline

def nqeen(row):
    global count
    if row == N:
        count += 1
        return
    
    for col in range(N):
        if not col_used[col] and not diag1[row - col + N] and not diag2[row + col]:
            col_used[col] = True
            diag1[row - col + N] = True
            diag2[row + col] = True
            
            nqeen(row + 1)
            
            col_used[col] = False
            diag1[row - col + N] = False
            diag2[row + col] = False

N = int(input())
col_used = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)
count = 0
nqeen(0)
print(count)