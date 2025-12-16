import sys

# 로컬 환경에서만 파일로 입력을 받고 싶을 때 (제출할 땐 주석 처리 필요)
sys.stdin = open("input.txt", "r")

# 빠른 입출력을 위해 input 함수를 덮어씌움
input = sys.stdin.readline

# --- 여기서부터 문제 풀이 작성 ---
N, M = map(int, input().split())

dic = set()
answer = []
for i in range(N):
    name = input().strip()
    dic.add(name)

for i in range(M):
    name = input().strip()
    if name in dic:
        answer.append(name)

answer.sort()
print(len(answer))

for item in answer:
    print(item)


import sys

# 로컬 환경에서만 파일로 입력을받고 싶을 때 (제출할 땐 주석 처리 필요)
sys.stdin = open("input.txt", "r")

# 빠른 입출력을 위해 input 함수를 덮어씌움
input = sys.stdin.readline

# --- 여기서부터 문제 풀이 작성---
N, M = map(int, input().split())

# 듣도 못한 사람 집합
unheard = set(input().strip() for _ in range(N))

# 보도 못한 사람 집합
unseen = set(input().strip() for _ in range(M))

# 듣보잡 = 교집합
answer = sorted(unheard & unseen)

print(len(answer))
print("\n".join(answer))
