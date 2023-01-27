#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = input('X = ')
Y = input('Y = ')
Z = input('Z = ')
if not(X or Y or Z) == (not X and not Y and not Z):
    print(True)
else:
    print(False)