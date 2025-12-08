import sys


input_string = sys.stdin.readline().strip()
find_string = sys.stdin.readline().strip()

last_c = find_string[-1]  # 찾는 데이터의 마지막 문자
fs_len = len(find_string)  # 찾는 데이터의 길이

data = list(input_string)

stack = []
for i in range(len(data)):
    # 스택에 데이터를 삽입
    stack.append(data[i])
    # 스택의 마지막 문자가 찾는 문자와 같고, 길이도 충분하다면
    if data[i] == last_c and len(stack) >= fs_len:
        # 문자열과 맞는지 확인
        if find_string == "".join(stack[-fs_len:]):
            for _ in range(len(fs_len)):
                stack.pop()  # 맞으면 모두 제거


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
