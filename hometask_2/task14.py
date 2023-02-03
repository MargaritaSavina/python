# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
num = int(input("Введите число N: "))
res = 1
degree = 0
while res <= num:
    print(f'2^{degree} = {res}')
    degree += 1
    res = 2**degree