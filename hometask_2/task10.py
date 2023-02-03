# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
from random import randint
num = int(input("Введите колическтво монет: "))
coins = []
for i in range(num):
    coins.append(randint(0,1))
print(*coins, sep=',')
count = 0   
for i in range(num):
    if coins[i] > 0:
        count += 1
if count >= num/2:
    print(f'{num - count} монет ')
else:
    print(f'{count} монет ')
