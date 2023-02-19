# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint
num = int(input("Введите размер массива: "))
left_num = int(input("Введите левую границу: "))
right_num = int(input("Введите правую границу: "))
list_num = []
for i in range(num):
    list_num.append(randint(-50,51))
print(list_num)
for i in range(num):
    if  list_num[i] >= left_num and right_num >= list_num[i]:
        print(list_num.index(list_num[i]),end= " ")
