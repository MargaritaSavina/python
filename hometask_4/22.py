# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
num1 = int(input("Введите кол-во элементов первого множества: "))
num2 = int(input("Введите кол-во элементов второго множества: "))
list1 = [input("множествo 1: " ) for i in range(num1)]
list2 = [input("множествo 2: " ) for i in range(num2)]
print(list1)
print(list2)
list3 = set(list1).intersection(list2)
print(sorted(list3))