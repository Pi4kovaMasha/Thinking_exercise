input_text = True
while input_text:
    n, m = map(int, input('Введите: ').split(' '))
    cones = list(map(int, input('Введите стоимость колбочек через пробел: ').split(' ')))
    if len(cones) == n:
        min_sum = sum(cones[:m])
        min_cones = m
        correct_sum = sum(cones[:m])
        for i in range(n - m):
            correct_sum = correct_sum - cones[i] + cones[min_cones - 1]
            if correct_sum < min_sum:
                min_sum = correct_sum
                break
            min_cones += 1
        print(min_cones)
        input_text = False
    else:
        print('Вы ввели неправильное количество стоимостей колбочек.')