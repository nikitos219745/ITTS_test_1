'''
Вводиться натуральне число M. Знайти та вивести факторіал M. (0 < M ≤ 13)
'''
M = int(input('Введіть М від 1 до 13: '))
fac = 1
if 0 < M <= 13:
    for i in range(2, M+1):
        fac *= i
    print('Факторіал',M,'=',fac)
else:
    print('Не правильне значення М')