N = int(input())
A, B, C, D, E, F = map(int, input().split())
dice = [A, B, C, D, E, F]

one_side_count = (N - 2) * (5 * N - 6)
two_side_count = (N - 2) * 4 + (N - 1) * 4
three_side_count = 4

if N == 1:
    print(sum(dice) - max(dice))

else:
    selected = [min(dice[0], dice[5]),
                min(dice[1], dice[4]),
                min(dice[2], dice[3])]
    selected.sort()
    ans = one_side_count * selected[0] + two_side_count * sum(selected[:2]) + three_side_count * sum(selected)

    print(ans)