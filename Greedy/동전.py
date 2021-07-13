N, K = input().split(' ')
N = int(N)
K = int(K)
count = 0

coin_list = []

for i in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

for coin in coin_list:
    count += K//coin
    K %= coin
    if K == 0:
        break

print(count)