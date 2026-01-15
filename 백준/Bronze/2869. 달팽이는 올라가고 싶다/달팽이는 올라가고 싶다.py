import sys

A, B, V = map(int, sys.stdin.readline().split())


def solutions(day, night, goal):
    if goal <= day:
        return 1

    work = goal - day
    oneday = day - night

    if work % oneday:
        return (work // oneday) + 2
    else:
        return (work // oneday) + 1


answer = solutions(A, B, V)
print(answer)
