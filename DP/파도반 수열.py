T = int(input())

for case in range(T):
    N = int(input())
    records = [0] * (N + 2)

    if N > 3:
        for i in range(4):

            if i == 3:
                records[i] = 2
            else:
                records[i] = 1

        for i in range(3, N):
            records[i] = records[i-3] + records[i-2]

        print(records[N-1])

    else:
        print(1)