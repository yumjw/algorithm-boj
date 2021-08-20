# https://www.acmicpc.net/problem/1052
# 걍 문제 자체를 잘못 이해했네...나가 죽어...
N, K = map(int, input().split())

if N <= K:
    print(0)

else:
    count = 0
    liter_standard = 1

    while N > K:
        lefts = N % 2
        N = N // 2
        if lefts == 0:
            liter_standard *= 2
        else:
            count += liter_standard
            liter_standard *= 2
            N += 1

    print(count)



# N, K = map(int, input().split())
# def cheak(num):
#     ans=0
#     while True:
#         a = num // 2
#         b = num % 2
#         ans += b
#         num = a
#         if num == 0:
#             break
#     return ans
#
#
# if N <= K:
#     print(0)
# else:
#     i = N
#     while True:
#         if cheak(i) <= K:
#             print(i-N)
#             break
#         else:
#             i += 1