'''
Вводиться ціле число A. Знайти і вивести суму його цифр. (0 ≤ A ≤ 1000000)
'''
m = int(input())
if 0 <= m <= 1000000:
    b = str(m)
    z = list(b)
    n = list(map(int, z))
    sum_n = sum(n)
    print(sum_n)
else: print('Неправильно введені дані')