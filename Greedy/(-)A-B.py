A, B = map(int, (input().split()))

count = 0
unable = False

while True:
    if B % 2 != 0 and B % 10 != 1:
        unable = True
        break

    elif B % 2 == 0 and B % 10 != 1:
        B = int(B / 2)
        count += 1

    elif B % 2 != 0 and B % 10 == 1:
        B = int(B//10)
        count += 1


if unable:
    print(-1)

else:
    print(count+1)