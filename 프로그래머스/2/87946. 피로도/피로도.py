from itertools import permutations


def solution(k, dungeons):
    max_clear = -1
    for perm in list(permutations(dungeons)):
        life = k
        clear_cnt = 0
        for dungeon in perm:
            # dungeon = [80, 20]
            if life < dungeon[0]:
                break

            clear_cnt += 1
            life -= dungeon[1]
        max_clear = max(max_clear, clear_cnt)
    print(max_clear)
    return max_clear
