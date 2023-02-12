# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
num = int(input("Введите количество элементов в списке: "))
list_num = []
for i in range(num):
    list_num.append(randint(0,10))
print(list_num)
def Product_pairs_num(list_numbers,numb):
    if numb%2 == 0:
        numb = numb // 2
    else:
        numb = numb // 2 + 1
    result = [list_numbers[i] * list_numbers[len(list_numbers) - 1 - i] for i in range(numb)]
    return result
print(Product_pairs_num(list_num,num))