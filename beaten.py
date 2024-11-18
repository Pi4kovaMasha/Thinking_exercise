n = int(input('Введите количество наборов входных данных: '))
list = []
for i in range(n):
    m = int(input('Введите количество красок: '))
    sum = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            sum = sum + (i&j)
    list.append(sum)
for i in list:
    print(i)