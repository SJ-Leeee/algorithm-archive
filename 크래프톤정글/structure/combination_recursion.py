count = 0


def combination_recursive(arr, result, start, depth, r):
    global count
    # 기저 조건: r개를 다 선택했으면 출력
    if depth == r:
        count += 1
        print(result)
        return

    # start부터 끝까지의 원소들을 시도
    for i in range(start, len(arr)):
        result[depth] = arr[i]  # 현재 원소 선택
        combination_recursive(arr, result, i + 1, depth + 1, r)
        # 백트래킹은 자동으로 됨 (result[depth]를 덮어씀)
    return count


arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]
result = [0] * 7
r = 7
a = combination_recursive(arr, result, 0, 0, 7)

print(a)
