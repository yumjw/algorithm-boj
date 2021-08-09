# T = int(input())

N = 3
fibonacci_list = [0] * (N+2)
count_list = [0] * (N+2)

def fibonacci_func(N):
    if N == 0:
        count_list[0] += 1
        return 0

    if N == 1 or N == 2:
        count_list[N] += 1
        return 1

    if fibonacci_list[N] != 0:
        count_list[N] += 1
        return fibonacci_list[N]
    fibonacci_list[N] = fibonacci_func(N-1) + fibonacci_func(N-2)
    return fibonacci_list[N]

fibonacci_func(N)
print(count_list)