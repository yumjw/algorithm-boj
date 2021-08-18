L, R = map(int, input().split())
minimum_eight = 0

digit_L = len(str(L))-1
digit_R = len(str(R))-1

if digit_R == digit_L:

    str_L = str(L)
    str_R = str(R)
    count = 0

    if str_L[0] != str_R[0]:
        print(0)
    else:
        if str_L[0] == '8':
            count += 1

        for i in range(1, len(str_L)):
            if str_L[i] != str_R[i]:
                break
            else:
                if str_L[i] == '8':
                    count += 1
        print(count)

else:
    print(0)