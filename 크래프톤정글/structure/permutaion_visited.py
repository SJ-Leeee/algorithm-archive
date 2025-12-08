# 원본 배열은 그대로 두고, 별도의 결과 배열에 순열을 만듦
# visited 배열로 이미 사용한 원소를 체크
# 매번 전체 배열을 돌면서 사용하지 않은 원소를 찾음
count = 0


def permutation_visited(arr, result, visited, depth, r):
    global count
    if depth == r:
        print(result)
        print(visited)
        count += 1
        return

    for i in range(len(arr)):  # 항상 모든원소를 순회
        if not visited[i]:  # 원소가 선택되지 않았더라면
            visited[i] = True  # 해당원소 사용
            result[depth] = arr[i]  # 현재깊이에 원소사용
            permutation_visited(arr, result, visited, depth + 1, r)  # 다음깊이 순회
            visited[i] = False  # 해당원소 사용중지


arr = [1, 2, 3, 4]
r = 2
result = [0 for _ in range(r)]
visited = [False for _ in range(len(arr))]
depth = 0
permutation_visited(arr, result, visited, depth, r)
print(count)
