n = int(input('Введите количество чисел в массиве: '))
inputtext = True
while inputtext:
    sequence = list(map(int, input('Введите последовательность красок через пробел: ').split(' ')))
    min = 1
    j = 0
    i = 0
    if len(sequence)==n:
        while i < n:
            if sequence[i] == min:
                while sequence[j] < sequence[j + 1]:
                    j+=1
                min+=1
                i += j+1
            elif min > 0:
                print(min-1)
                break
            if i == sequence[-1]:
                print(min)
                break
        inputtext = False
    else:
        print('Вы ввели не правильную последовательность красок, попробуйте ещё раз.')