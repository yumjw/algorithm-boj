#구현 실패: 만약 다음 도시의 기름값이 현재 도시보다 비싸다면 그 도시까지 다 넣고 출발한다.
#아이디어를 너무 복잡하게 생각하는 것 같다! min price를 미리 설정해두면 피곤할 일이 없다....
N = int(input())
road_distance = list(map(int, input().split()))
gasoline_price = list(map(int, input().split()))

current_city_index = 0
next_city_index = 1

cumulative_distance = 0
price_total = 0
sustain_current = False

while next_city_index < N:

    if not sustain_current:
        cumulative_distance += road_distance[current_city_index]

    current_city_price = gasoline_price[current_city_index]
    next_city_price = gasoline_price[next_city_index]

    if current_city_price < next_city_price:

        cumulative_distance += road_distance[next_city_index]
        next_city_index += 1
        sustain_current = True

    else:

        price_total += cumulative_distance * gasoline_price[current_city_index]
        cumulative_distance = 0
        current_city_index = next_city_index
        next_city_index += 1
        sustain_current = False

print(price_total)