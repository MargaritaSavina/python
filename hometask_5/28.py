# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
num1 = int(input("Введите число1: "))
num2 = int(input("Введите число2: "))
def Sum(a,b):
    if b == 0:
        return a 
    return 1 + Sum(a,b-1)

print(Sum(num1,num2))