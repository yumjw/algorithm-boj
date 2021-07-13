# -가 나타나서 다시 -가 나타나기 전까지 괄호 치기.
expression_list = list(input().split('-'))

first_value = sum(list(map(int, expression_list.pop(0).split('+'))))

for i in expression_list:
    first_value -= sum(list(map(int, i.split('+'))))

print(str(first_value))
