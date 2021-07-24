S = int(input())

Number = 1
N = 0

while S > 0:
    if S - Number > Number:
        S -= Number
        Number += 1
        N += 1
    else:
        N += 1
        break

print(N)