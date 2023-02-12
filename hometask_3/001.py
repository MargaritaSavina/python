# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
num = int(input("Введите количество элементов в списке: "))
list_num = []
for i in range(num):
    list_num.append(randint(0,10))
print(list_num)
def Sum_odd(list_numbers):
    sum = 0
    for i in range(0,len(list_numbers),1): 
        if i % 2 == 1:
            sum += list_numbers[i]
    return sum
print("Сумма чисел на нечетных позициях = ", Sum_odd(list_num))
