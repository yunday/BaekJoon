# def t1():
#     for a in range(10):
#         if 2 * a == int(n):
#             return a
#     return 0
#
#
# def t2():
#     for a in range(10):
#         for b in range(10):
#             if 11 * a + 2 * b == int(n):
#                 return 10 * a + b
#     return 0
#
#
# def t3():
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 if 101 * a + 11 * b + 2 * c == int(n):
#                     return 100 * a + 10 * b + c
#     return 0
#
#
# def t4():
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 for d in range(10):
#                     if 1001 * a + 101 * b + 11 * c + 2 * d == int(n):
#                         return 1000 * a + 100 * b + 10 * c + d
#     return 0
#
#
# def t5():
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 for d in range(10):
#                     for e in range(10):
#                         if 10001 * a + 1001 * b + 101 * c + 11 * d+2 * e == int(n):
#                             return 10000 * a + 1000 * b + 100 * c + 10 * d + e
#     return 0
#
#
# def t6():
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 for d in range(10):
#                     for e in range(10):
#                         for f in range(10):
#                             if 100001 * a + 10001 * b + 1001 * c + 101 * d+11 * e + 2 * f == int(n):
#                                 return 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
#     return 0
#
#
# n = input()
#
# if len(n) == 1:
#     print(t1())
# elif len(n) == 2:
#     print(t2())
# elif len(n) == 3:
#     print(t3())
# elif len(n) == 4:
#     print(t4())
# elif len(n) == 5:
#     print(t5())
# elif len(n) == 6 or n == '1000000':
#     print(t6())

# 좋은 코드
# 노가다 말고 어떻게든 찾기....... 난 생각도 못함 ㅠㅠ
N = int(input())
maker = 0

for i in range(max(1, N - 60), N + 1):
    li = list(map(int, str(i)))
    if sum(li, i) == N:
        maker = i
        break

print(maker)
