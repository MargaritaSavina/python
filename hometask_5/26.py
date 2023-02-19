# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
num1 = int(input("Введите число1: "))
num2 = int(input("Введите число2: "))
def Product(a,b):
    if b == 1:
        return a 
    return a * Product(a,b-1)

print(Product(num1,num2))
