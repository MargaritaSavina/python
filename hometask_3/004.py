# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
num = int(input("Введите число: "))
def Binary_num(numb):
    list_binary = []
    count = 0
    numb2 = numb
    while numb2 > 0:
            numb2 = numb2 // 2
            count += 1
    for i in range(count):
        list_binary.append(numb % 2)
        numb = numb // 2
    list_binary.reverse()
    return list_binary
print(Binary_num(num))
