"""
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
"""


def solution(fees, records):
    answer = []

    fee_time, fee_price, add_time, add_price = fees
    in_time_dict = {}
    is_exit = {}
    acc_dict = {}
    for i in records:
        # 시간, 차번호, 행동
        now_time, car_num, act = i.split()
        h, m = now_time.split(":")
        cal_time = 60 * int(h) + int(m)

        if act == "IN":
            in_time_dict[car_num] = cal_time
            is_exit[car_num] = False
        else:
            use_time = cal_time - in_time_dict[car_num]  # 사용한 시간
            is_exit[car_num] = True  # 나갔는지

            if car_num in acc_dict:  # 사용한시간 정리
                acc_dict[car_num] += use_time
            else:
                acc_dict[car_num] = use_time

    for key, value in is_exit.items():
        if value == False:
            if key in acc_dict:
                acc_dict[key] += 1439 - in_time_dict[key]
            else:
                acc_dict[key] = 1439 - in_time_dict[key]

    for key, value in acc_dict.items():
        price = fee_price
        over_unit = (
            0 if value - fee_time < 0 else (value - fee_time + add_time - 1) // add_time
        )

        price = price + add_price * over_unit
        answer.append((int(key), price))
    answer.sort()
    real_answer = []
    for _, price in answer:
        real_answer.append(price)

    return real_answer


exam = ["00:00 1234 IN"]
fees = [1, 461, 1, 10]
solution(fees, exam)
