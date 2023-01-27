# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
numbX1 = float(input('A = '))
numbY1 = float(input())
numbX2 = float(input('B = '))
numbY2 = float(input())
distance = math.sqrt((numbX2 - numbX1)**2 + (numbY2 - numbY1)**2)
print('Расстояние = ', round(distance,3))