# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
oper = input('Введите операцию между х и у: ')
rows = int(input('Введите х: '))
columns = int(input('Введите y: '))

def print_operation_table(operation, num_rows, num_columns):
    for x in range(1,num_rows+1,1):
        for y in range(1,num_columns+1,1):
            res = dict_operations[operation]
            print(res(x,y),end='     ')
        print()
               


dict_operations = { '+': lambda x,y: x + y,
                    '/': lambda x,y: x / y,
                    '//': lambda x,y: x // y,
                    '-' : lambda x,y: x - y,
                    '*' : lambda x,y: x * y,
                    '**' : lambda x,y: x ** y,
                   }
print(print_operation_table(oper,rows,columns))

# x = 6
# y = 6
# list1 = []
# print(list1)
# # print_operation_table = list(map(lambda x, y: x * y, list1))
# # print(print_operation_table)
# a = 6
# for x in range(1,a+1,1):
#     for y in range(1,a+1,1):
#         list1.append(x*y)
# print(list1)   
    