A, B = map(int, (input().split()))

count = 0
unable = False

while B > A:
    if B % 2 != 0 and B % 10 != 1:
        count = -1
        break

    elif B % 2 == 0 and B % 10 !=1:
        B = int(B / 2)
        count += 1

    elif B % 2 != 0 and B % 10 ==1:
        B = int(B//10)
        count += 1

    if A != B:
        count = -1

if count == -1:
    print(count)

else:
    print(count+1)