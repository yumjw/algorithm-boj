# 한번만 쭉 가도 된다.
# 다만 시작할 때 경우의 수를 나눠서 고려해야 한다.

N = int(input())
count = 0

def status_change(status):
    return 1-status

current_status = [0] + list(map(int, list(input()))) + [0]
object_status = [0] + list(map(int, list(input()))) + [0]
