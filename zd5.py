def summa_variables(first, last, variables, sum):
    for j in range(int(first), int(last)+1):
        sum += variables[f"x{j}"]
    return sum

n, m = map(int, input('Введите количество песен и количество предпочтней по настроению: ').split(' '))

pereferences = []
for _ in range(m):
    line = input('Введите предпочте по настроению: ').split(' ')
    pereferences.append(line)

variables = {}
for i in range(1, n + 1):
    variables[f"x{i}"] = 0

for first, last, operator, summa in pereferences:
    summa = int(summa)
    sum = 0
    sum = summa_variables(first, last, variables, sum)
    if operator==">=":
        while sum < summa:
            for i in range(int(first), int(last)+1):
                variables[f"x{i}"]+=1
            sum = summa_variables(first, last, variables, 0)
    if operator=="<=":
        while sum > summa:
            for i in range(int(first), int(last)+1):
                variables[f"x{i}"]-=1
            sum = summa_variables(first, last, variables, 0)
yes = 0
for first, last, operator, summa in pereferences:
    summa = int(summa)
    sum = summa_variables(first, last, variables, 0)
    if operator==">=" and sum>=summa:
        yes+=1
    elif operator=="<=" and sum<=summa:
        yes+=1
    else:
        print(f"Не сработало на {first}, {last}, {operator}, {summa}")

if yes == m:
    print('YES')
else:
    print("NO")