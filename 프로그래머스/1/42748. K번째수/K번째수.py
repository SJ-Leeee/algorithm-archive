# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
def solution(array, commands):
    answer = []
    for cmd in commands:
        start, end, rank = cmd
        tmp_arr = array[start - 1 : end]
        tmp_arr.sort()
        answer.append(tmp_arr[rank - 1])
    
    return answer