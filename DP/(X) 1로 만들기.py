# https://www.acmicpc.net/submit/1463
# 무작정 조건문을 이용하면...+1을 무식하게 많이 하는 경우의 수가 생긴다. DP 써라.
N = int(input())
memoization = [0] * (N+1)

for i in range(2, N+1):
    memoization[i] = memoization[i - 1] + 1
    if i % 2 == 0:
        memoization[i] = min(memoization[i], memoization[i // 2] + 1)
    if i % 3 == 0:
        memoization[i] = min(memoization[i], memoization[i // 3] + 1)

print(memoization[N])