N = int(input())
count = 0

while N >= 15:
    N -= 5
    count += 1

while N > 0:
    if N % 3 == 0:
        count += N//3
        N=0
        break
    else:
        N -= 5
        count +=1

if N == 0:
    print(count)
else:
    print(-1)


# Best Solution
# 5부터 말고 3부터 접근했으면 좋았다.

sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else :
    print(-1)