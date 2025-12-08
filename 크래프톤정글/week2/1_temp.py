# first_word = input("첫 단어를 입력하세요: ")

# while 1:
#     last_word = input("끝말단어를 입력해주세요: ")
#     if last_word == "종료":
#         break

#     if first_word[len(first_word) - 1] != last_word[0]:
#         print("다시 입력해주세요")

#     first_word = last_word


# # app = "가나다라마바"

# # print(app[len(app) - 1])


# def get_prime_number(n):

#     if n == 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     for i in range(5, n // 2 + 1, 2):

#         if (n % i) == 0:
#             return False

#     return True


# result = 0
# testcase = [23, 152, 12312, 4124, 11, 16, 337, 1111, 97, 101, 103, 107, 109, 113]
# # for n in testcase:
# #     result += get_prime_number(n)
# #     print(result)


# """
# 1. n은 짝수면 안된다.
# 2. n의 절반보다 작은 숫자에 약수가 있다.
# 4. 하지만 2,3,5,7,11,13,17,19 의 배수로는 나누지 않아도된다.
# """

# print(get_prime_number(4))
# print(get_prime_number(6))
# print(get_prime_number(8))
# print(get_prime_number(10))

# print(get_prime_number(9))
# print(get_prime_number(15))
# print(get_prime_number(21))

# print(get_prime_number(25))
# print(get_prime_number(49))


# def sum_only_int(list):
#     sum = 0
#     for i in list:
#         if isinstance(i, bool):
#             continue
#         if isinstance(i, int):
#             print(i)
#             sum += i

#     return sum


# baaa = [12, 1.2, True, -0.1, -5, ("나는", "바보입니다"), "3"]

# result = sum_only_int(baaa)
# print(result)


# def classify_by_type(list):
#     result = {}

#     for item in list:
#         type_name = type(item).__name__

#         if type_name in result:
#             result[type_name].append(item)
#         else:
#             result[type_name] = [item]

#     print(result)


# classify_by_type(
#     [
#         1,
#         2,
#         -1,
#         "dsd",
#         "1231gg",
#         True,
#         False,
#         {"key": "value"},
#         (12, "가나다"),
#         [1, 2, "콜미"],
#     ]
# )


# def countdown(n):
#     if n <= 0:
#         print("펑펑")
#     else:
#         print(n)
#         countdown(n - 1)


# def fact(n):
#     if n == 1:
#         return 1

#     return n * fact(n - 1)


memory = {}


def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


# import time

# start1 = time.time()
# a = fibonacci(1000)
# print(a)
# end1 = time.time()
# print(f"첫번째 거 {end1- start1} 초")


# def fibonacci2(n, memo={}):
#     if n in memo:
#         return memo[n]  # 이미 계산된 값 재사용

#     if n <= 1:
#         result = n
#     else:
#         result = fibonacci2(n - 1, memo) + fibonacci2(n - 2, memo)

#     memo[n] = result  # 계산 결과 저장
#     return result


# start2 = time.time()
# b = fibonacci2(500)
# print(b)
# end2 = time.time()
# print(f"두번째 거 {end2 - start2} 초")


# class Calcurator:
#     def __init__(self, num):
#         self.num = num

#     def intro(self):
#         print(f"{self.num}번 입력")


# num1 = Calcurator(1)
# num2 = Calcurator(2)
# num3 = Calcurator(3)
# num4 = Calcurator(4)

# print(type(num1).__name__)

# num1.intro()
# num2.intro()
# num3.intro()
# num4.intro()


# class User:
#     user_count = 0

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         User.user_count += 1

#     @classmethod
#     def get_user_count(cls):
#         return cls.user_count

#     @classmethod
#     def from_string(cls, user_string):
#         # "이름,이메일" 형태의 문자열로 인스턴스 생성
#         name, email = user_string.split(",")
#         return cls(name.strip(), email.strip())

#     @staticmethod
#     def is_valid_email(email):
#         # 간단한 이메일 검증 (실제로는 더 복잡한 로직 필요)
#         return "@" in email and "." in email


# # 사용 예시
# user1 = User("김철수", "kim@example.com")
# user2 = User.from_string("이영희, lee@example.com")

# print(User.get_user_count())  # 2
# print(User.is_valid_email("test@email.com"))  # True

# count_zero = 0
# count_one = 0


# def fibonacci(n):
#     global count_zero
#     global count_one

#     if n == 0:
#         count_zero += 1
#         return 0
#     elif n == 1:
#         count_one += 1
#         return 1
#     else:
#         return


# fibonacci(22)

# print(count_zero)
# print(count_one)


# count_zero = 0
# count_one = 0


# def fibonacci(n):
#     n
#     count_zero
#     for i in range(1,n)

#     0 = n-2
#     1 = n-1
# T = int(input())

# for _ in range(T):
#     n = map(int, input().split())
#     result = fibonacci(n)
#     print(result)

# 472
# 385


# def cal3(num1, num2):
#     hundreds_digit = num2 // 100
#     tens_digit = num2 % 100 // 10
#     ones_digit = num2 % 10

#     answer_3 = ones_digit * num1
#     answer_4 = tens_digit * num1
#     answer_5 = hundreds_digit * num1
#     answer_6 = answer_5 * 100 + answer_4 * 10 + answer_3

#     print(answer_3)
#     print(answer_4)
#     print(answer_5)
#     print(answer_6)

#     return


# cal3(472, 385)


# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.


# def check_grade(score):
#     if 90 <= score <= 100:
#         print("A")
#     elif 80 <= score <= 89:
#         print("B")
#     elif 70 <= score <= 79:
#         print("C")
#     elif 60 <= score <= 69:
#         print("D")
#     else:
#         print("F")


# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.


# def check_yun_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(1)
#     else:
#         print(0)


# check_yun_year(1972)


# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.


# def shortest_distance(x, y, w, h):
#     left_x = x
#     right_x = w - x

#     up_y = h - y
#     down_y = y

#     answer = min(left_x, right_x, up_y, down_y)

#     print(answer)


# shortest_distance(161, 181, 762, 375)


# def product9(num):
#     for i in range(10):
#         print(f"{num} * {i} = {num*i}")


# 10 5
# 1 10 4 9 2 3 8 5 7 6

# max_num = -1
# index = -1

# for i in range(1, 10):
#     num = int(input())
#     if num > max_num:
#         max_num = num
#         index = i

# print(max_num)
# print(index)

# N = int(input())

# def score_check(answer_list):
#     result = 0
#     for check in answer_list:
#         if len(check) > 0:
#             for i in range(1, len(check) + 1):
#                 result += i

#     print(result)


# for _ in range(N):
#     input_data = input()
#     answer_list = input_data.split("X")
#     score_check(answer_list)


# print(sum((1, 2, 3)))
# N = int(input())
# test = [
#     [5, 50, 50, 70, 80, 100],
#     [7, 100, 95, 90, 80, 70, 60, 50],
#     [3, 70, 90, 80],
#     [3, 70, 90, 81],
#     [9, 100, 99, 98, 97, 96, 95, 94, 93, 91],
# ]

# for i in range(len(test)):
#     # data = list(map(int, input().split()))
#     data = test[i]
#     n = data[0]
#     scores = data[1:]

#     pass_count = 0
#     average = round(sum(scores) / n, 3)

#     for score in scores:
#         if score > average:
#             pass_count += 1

#     pass_ratio = round((pass_count / n) * 100, 3)
#     print("{:.3f}".format(pass_ratio))

# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# product = num1 * num2 * num3
# product_str = str(product)

# dictionary = {}

# for num in product_str:
#     if num in dictionary:
#         dictionary[num] += 1
#     else:
#         dictionary[num] = 1

# for _ in len(dictionary):


# n = int(input())
# numbers = list(map(int, input().split()))
# result = 0


# def get_prime_number(n):

#     if n == 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     for i in range(5, n // 2 + 1, 2):

#         if (n % i) == 0:
#             return False

#     return True


# def goldbah(num):
#     half = num // 2

#     for i in range(half, 0, -1):
#         if get_prime_number(i) and get_prime_number(num - i):
#             print(f"{i} {num - i}")
#             return


# # N = int(input())

# # for _ in range(N):
# #     num = int(input())
# #     goldbah(num)

# goldbah(12)


# class Slime:
#     obj_number = 1

#     def __init__(self):
#         self.hp = 80
#         self.number = Slime.obj_number
#         self.defence = 0.8
#         self.attack_power = 1
#         Slime.obj_number += 1

#     def attack(self, enemy, count=1):
#         attack_power = self.attack_power - enemy.defence
#         enemy.hp -= attack_power * count
#         print(enemy.hp)

#     def info(self):
#         print(f"나는 {self.number} 호 슬라임이다!!")


# class FireSlime(Slime):
#     fire_slime_obj_number = 1

#     def __init__(self):
#         super().__init__()
#         self.attack_power = 4

#     def attack(self, enemy, count=1):
#         attack_power = self.attack_power * 2 - enemy.defence
#         enemy.hp -= attack_power * count
#         print(enemy.hp)


# slime_1 = Slime()
# slime_2 = Slime()
# slime_3 = Slime()

# slime_1.info()
# slime_2.info()
# slime_3.info()

# fire_slime_1 = FireSlime()

# fire_slime_1.attack(slime_3)
# slime_1.attack(slime_2, 100)


# product = 1
# for _ in range(3):
#     num = int(input())
#     product *= num

# dictionary = {}
# product_str = str(product)
# for num in product_str:
#     if num in dictionary:
#         dictionary[num] += 1
#     else:
#         dictionary[num] = 1

# for i in range(10):
#     key = dictionary.get(str(i)) or 0
#     print(f"{key}")

# num = int(input())


# def hansu(num):
#     if num == 0:
#         print(0)
#         return
#     if num < 100:
#         print(num)
#         return
#     hundreds_digit = num // 100
#     tens_digit = num % 100 // 10
#     ones_digit = num % 10

#     result = 99
#     sub = tens_digit - hundreds_digit

#     if 0 < tens_digit + sub and tens_digit + sub <= ones_digit < 10:
#         result += 1

#     if hundreds_digit != 1:
#         result += (hundreds_digit - 1) * 5

#     while tens_digit > 0:
#         sub = tens_digit - hundreds_digit
#         if 0 <= ones_digit + sub < 10:
#             result += 1
#         tens_digit -= 1

#     print(result)
#     return


# hansu(num)


# if hundreds_digit != 1:
#         result += (hundreds_digit - 1) * 5

#     sub = tens_digit - hundreds_digit

#     if 0 <= ones_digit + sub < 10:
#         if ones_digit >= ones_digit + sub:
#             result += 1

#     while tens_digit > 0:
#         sub = tens_digit - hundreds_digit

#         if 0 <= ones_digit + sub < 10:
#             result += 1
#         tens_digit -= 1

# 10 8
# 3
# 0 3
# 1 4
# 0 2

# w, h = map(int, input().split())
# N = int(input())
# x_arr = [w]
# y_arr = [h]

# for _ in range(N):
#     direct, cut = map(int, input().split())
#     if direct:
#         x_arr.append(cut)
#     else:
#         y_arr.append(cut)

# x_arr = sorted(x_arr)
# y_arr = sorted(y_arr)

# result = []

# for i in range(len(x_arr)):
#     if i == 0:
#         x = x_arr[i]
#     else:
#         x = x_arr[i] - x_arr[i - 1]

#     for j in range(len(y_arr)):
#         if j == 0:
#             y = y_arr[j]
#         else:
#             y = y_arr[j] - y_arr[j - 1]
#         result.append(x * y)

# print(max(result))
# # 0이면 그냥 두고 0 아니면 다음거랑


# import timeit

# # 긴 문자열 생성
# long_string = "a" * 1000000


# # 해시 계산 시간 측정
# def measure_hash_performance():
#     # 첫 번째 해시 계산 (실제 계산)
#     start = timeit.default_timer()
#     hash1 = hash(long_string)
#     first_time = timeit.default_timer() - start

#     # 두 번째 해시 계산 (캐싱된 값)
#     start = timeit.default_timer()
#     hash2 = hash(long_string)
#     second_time = timeit.default_timer() - start

#     print(f"첫 번째 해시 계산: {first_time:.8f}초")
#     print(f"두 번째 해시 계산: {second_time:.8f}초")
#     print(f"속도 향상: {first_time/second_time:.2f}배")
#     print(f"해시값 동일: {hash1 == hash2}")


# import timeit


# def benchmark_string_methods():
#     # f-string vs format
#     setup = "name = 'Alice'; age = 25"

#     fstring_time = timeit.timeit(
#         "f'Hello {name}, age {age}'", setup=setup, number=100000
#     )

#     format_time = timeit.timeit(
#         "'Hello {}, age {}'.format(name, age)", setup=setup, number=100000
#     )

#     print(f"f-string: {fstring_time:.4f}초")
#     print(f"format: {format_time:.4f}초")
#     print(f"f-string이 {format_time/fstring_time:.1f}배 빠름")


# benchmark_string_methods()


# 하노이의 탑

# 생각해보자 ..

"""
배열이 있다면
a: [1,2,3,4]
b: []
c: []

4는 c로 가야한다.
    swap(3, b) => 3미만의 숫자들을 b로 보낸다
        swap(2, c) => 2이하의 숫자들을 c로 보낸다
            for n in range(1, num+1):
                swap(n, b)
            swap(1, b) => 1이하의 숫자들을 b로 보낸다  스왑 안에는 if num == b.push(1))


    3은 b로 가고싶다.
        1, 2 는 c로 가야한다.
        2는 c로 가고싶다.
            1은 b로 가야한다.
"""


# def swap(num, location_num, destination_num):
# 1이라면 바로 옮겨라
# if num == 1:
#     print(f"{num} 은 {location_num}에서 {destination_num}로 이동했습니다. ")
#     return

# # 새로운 위치
# new_destination = 6 - location_num - destination_num

# # 새로운 위치로 num-1을 이동시켜라
# swap(num - 1, location_num, new_destination)

# # 그리고 내가 그 위치로 가라
# print(location_num, destination_num)

# 다시 나보다 작은 숫자를 내쪽으로 옮겨라
#     swap(num - 1, location_num, destination_num)

# count = 0


# def swap(num, location_num, destination_num, N):
#     global count
#     count = count + 1
#     if num == 1:
#         if N <= 20:
#             print(f"{location_num} {destination_num}")
#         return

#     # 새로운 위치 (임시 위치)
#     new_destination = 6 - location_num - destination_num

#     # 위의 n-1개를 임시 위치로 이동
#     swap(num - 1, location_num, new_destination)

#     # 가장 큰 원판을 목표 위치로 이동
#     print(f"{location_num} {destination_num}")

#     # 임시 위치의 n-1개를 목표 위치로 이동
#     swap(num - 1, new_destination, destination_num)  # 여기가 핵심!
#     return


# swap(7, 1, 3)
# print(count)


# count = 0


# def swap(num, location_num, destination_num, N):
#     global count
#     count = count + 1
#     # 1이라면 바로 옮겨라
#     if num == 1:
#         if N <= 20:
#             print(f"{location_num} {destination_num}")
#         return

#     # 새로운 위치
#     new_destination = 6 - location_num - destination_num

#     # 새로운 위치로 n-1 이동
#     swap(num - 1, location_num, new_destination, N)

#     # 그리고 n이 그 위치로
#     if N <= 20:
#         print(f"{location_num} {destination_num}")

#     # n보다 작은 숫자들을 현재위치로
#     swap(num - 1, new_destination, destination_num, N)
#     return


# num = int(input())
# swap(num, 1, 3, num)
# print(count)


# count = 0


# def swap(num, location_num, destination_num, N):
#     global count
#     count = count + 1

#     if num == N:
#         print(count)

#     # 1이라면 바로 옮겨라
#     if num == 1:
#         if N <= 20:
#             print(f"{location_num} {destination_num}")
#         return

#     # 새로운 위치
#     new_destination = 6 - location_num - destination_num

#     # 새로운 위치로 n-1 이동
#     swap(num - 1, location_num, new_destination, N)

#     # 그리고 n이 그 위치로
#     if N <= 20:
#         print(f"{location_num} {destination_num}")

#     # n보다 작은 숫자들을 현재위치로
#     swap(num - 1, new_destination, destination_num, N)
#     return


# num = int(input())
# swap(num, 1, 3, num, False)
# print(count)


# count = 0


# def swap(num, location_num, destination_num, N, flag):
#     global count
#     count = count + 1

#     # 1이라면 바로 옮겨라
#     if num == 1:
#         if N <= 20 and flag:
#             print(f"{location_num} {destination_num}")
#         return

#     # 새로운 위치
#     new_destination = 6 - location_num - destination_num

#     # 새로운 위치로 n-1 이동
#     swap(num - 1, location_num, new_destination, N, flag)

#     # 그리고 n이 그 위치로
#     if N <= 20 and flag:
#         print(f"{location_num} {destination_num}")

#     # n보다 작은 숫자들을 현재위치로
#     swap(num - 1, new_destination, destination_num, N, flag)
#     return


# num = int(input())
# swap(num, 1, 3, num, False)
# print(count)
# swap(num, 1, 3, num, True)

# count = 0


# def swap(num, location_num, destination_num, N):
#     global count
#     count = count + 1

#     if num == 1:
#         if N <= 20:
#             print(f"{location_num} {destination_num}")
#         return

#     new_destination = 6 - location_num - destination_num

#     swap(num - 1, location_num, new_destination, N)

#     if N <= 20:
#         print(f"{location_num} {destination_num}")

#     swap(num - 1, new_destination, destination_num, N)

#     # 최초 호출이 끝날 때만 count 출력
#     if num == N:
#         print(count)
#     return


# num = int(input())
# swap(num, 1, 3, num)


# my_tuple[1] = 3
# print(my_tuple)

# my_dict = {"name": "Alice", "age": 25, "city": "New York", "job": "designer"}
# items = my_dict.items()

# print(type(items))
# print(list(items))


# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n - 1)


# start1 = time.time()
# fact1 = factorial(100)
# print(fact1)
# end1 = time.time()
# start2 = time.time()
# fact2 = math.factorial(100)
# print(fact2)
# end2 = time.time()
# print(f"{end1 - start1:.5f} sec")
# print(f"{end2 - start2:.5f} sec")


# N = int(input())
# arr = list()
# for _ in range(N):
#     num = int(input())
#     arr.append(num)


# arr.sort()
# for num in arr:
#     print(num)

# N = int(input())

# for _ in range(N):
#     char_list = []
#     n, s = input().split()
#     n = int(n)
#     for c in s:
#         char_list.append(c * n)
#     print("".join(char_list))


# N = input().strip()

# n_list = N.split(" ")

# print(len(n_list))

# import sys

# count = [0] * 10000


# N = int(sys.stdin.readline())
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     count[num] += 1

# for index, num in enumerate(count):
#     if num == 0:
#         continue
#     if num == 1:
#         print(index)
#     if num > 1:
#         char = (str(index) + "\n") * (num - 1) + str(index)
#         print(char)

# print(str(num_t) + "\n" * 4 + "3")

### 문자열정렬

# import sys

# N = int(input())
# duplicate_data = [sys.stdin.readline().strip()for i in range(N)]
# data=list(set(duplicate_data))
# data.sort(key=lambda x:(len(x), x))

# for i in data:
#     print(i)


"""
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""
"""
abcdefghijklmnopqrstuvwxyz
"""


# memory = {}


# def fibonacci(n):
#     if n in memory:
#         return memory[n]

#     if n <= 1:
#         return n

#     memory[n] = fibonacci(n - 1) + fibonacci(n - 2)
#     return memory[n]


# print(fibonacci(10000))

import time
import heapq
import random

# 테스트 데이터
data = [random.randint(1, 10000000) for _ in range(1000000)]

# 방법 1: 정렬
start = time.time()
result1 = sorted(data, reverse=True)[:10]
time1 = time.time() - start

# 방법 2: nlargest
start = time.time()
result2 = heapq.nlargest(10, data)
time2 = time.time() - start

print(f"정렬: {time1:.4f}초")  # 더 오래 걸림
print(f"nlargest: {time2:.4f}초")  # 더 빠름
