def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        record = graph[a][b][c]
        if record != -1:
            return record
        else:
            graph[a][b][c] = w(20,20,20)
            return graph[a][b][c]

    if a < b and b < c:
        record_c = graph[a][b][c-1]
        record_b = graph[a][b-1][c]
        record_a = graph[a-1][b][c]

        if record_a != -1 and record_b != -1 and record_c != -1:
            return record_a + record_b + record_c

        else:
            for a_,b_,c_ in [(a-1,b,c), (a,b-1,c), (a,b,c-1)]:
                if graph[a_][b_][c_] == -1:
                    graph[a_][b_][c_] = w(a_,b_,c_)

            return graph[a-1][b][c] + graph[a][b-1][c] + graph[a][b][c-1]

    record_1 = graph[a-1][b][c]
    record_2 = graph[a-1][b-1][c]
    record_3 = graph[a-1][b][c-1]
    record_4 = graph[a-1][b-1][c-1]

    if record_1 != -1 and record_2 != -1 and record_3 != -1 and record_4 != -1:
        return record_1 + record_2 + record_3 + record_4

    else:
        for a_,b_,c_ in [(a-1,b,c), (a-1,b-1,c), (a-1,b,c-1), (a-1,b-1,c-1)]:
            if graph[a_][b_][c_] == -1:
                graph[a_][b_][c_] = w(a_,b_,c_)

        return graph[a-1][b][c] + graph[a-1][b-1][c] + graph[a-1][b][c-1] + graph[a-1][b-1][c-1]

a,b,c = map(int, input().split())
graph = [[([-1]*21) for _ in range(21)] for _ in range(21)]

ans = w(a,b,c)
print(ans)