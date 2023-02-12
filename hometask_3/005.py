# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


num = int(input("Введите число: "))
list1 = []
fib1,fib2 = 0,1
i = num
while i >= 0:
    list1.append(fib1)
    fib1,fib2 = fib2,fib1 - fib2
    i -=1
list1.reverse()
fib1,fib2 = 0,1
i = 0
while i < num:
    fib1,fib2 = fib2,fib1 + fib2
    list1.append(fib1)
    i +=1
print(list1)