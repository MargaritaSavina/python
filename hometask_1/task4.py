#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).∞
numbQuarter = int(input('Введите номер четверти   '))
if numbQuarter > 4 or numbQuarter < 1:
    print('номер четверти ввeден неверно')
else:
    if numbQuarter == 1:
        print('X ∈ (0;∞)  Y ∈ (0;∞)')
    elif numbQuarter == 2:
        print('X ∈ (-∞;0)  Y ∈ (0;∞)')
    elif numbQuarter == 3:
        print('X ∈ (-∞;0)  Y ∈ (-∞;0)')
    else: 
        print('X ∈ (0;∞)  Y ∈ (-∞;0)')