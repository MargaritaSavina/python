# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной 
#части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
import random
num = int(input("Введите количество элементов в списке: "))
list_num = []
for i in range(num):
    list_num.append(round(random.gauss(0,10),3))
    #list_num[i] = round(random.gauss(0,1),3)
print(list_num)
list_num_res = []
for i in list_num:
    list_num_res.append(round((abs(i) % 1),3))
print(list_num_res)
min_num = min(list_num_res)
max_num = max(list_num_res)
print(" Разница между максим. и миним. значениями = ",round(max_num - min_num,3))