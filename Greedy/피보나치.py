T = int(input())

fibonacci = [0, 1, 1]
[fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(3, 100)]

def find_fivonacci(n):
    idx = 2
    while fibonacci[idx] <= n:
        idx += 1

    return fibonacci[idx-1]


for i in range(T):

    n = int(input())
    result_lst = []

    while n > 0:
        element = find_fivonacci(n)
        result_lst.append(element)
        n -= element

    result_lst.sort()
    str_lst = list(map(str, result_lst))
    print(' '.join(str_lst))