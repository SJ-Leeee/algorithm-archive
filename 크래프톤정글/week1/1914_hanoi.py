count = 0


def swap(num, location_num, destination_num, N):
    if num == 1:
        if N <= 20:
            print(f"{location_num} {destination_num}")
        return

    new_destination = 6 - location_num - destination_num

    swap(num - 1, location_num, new_destination, N)

    if N <= 20:
        print(f"{location_num} {destination_num}")

    swap(num - 1, new_destination, destination_num, N)

    return


num = int(input())

if num > 20:
    print(2**num - 1)
else:
    print(2**num - 1)
    swap(num, 1, 3, num)
# 수학 공식으로 바로 계산
