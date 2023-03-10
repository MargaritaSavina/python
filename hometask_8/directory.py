# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной\
def print_phone():
    with open('phone.txt','r', encoding='utf-8') as text:
            print(text.read())


def import_phone():
    phone = {}
    with open('phone.txt','r', encoding='utf-8') as text:
        s = text.readlines()
        for i in range(len(s)):
            phone[i] = s[i].split()    
        print(phone)
        s2 = input('Введите имя или номер для поиска:  ')
        for i in phone:
            if s2 in phone[i]:
                print(phone[i])
        
        
def export():
    with open('phone.txt','a', encoding='utf-8') as text:
        str_new = input('Введите новый контакт:  ')
        text.writelines(f'\n{str_new}')

def delete_cont():
    with open('phone.txt','r', encoding='utf-8') as text:
        s = text.readlines() 
    key = int(input("Введите id контакта для удаления: ")) 
    with open('phone.txt','w', encoding='utf-8') as txt:
        for line in s:
            if line not in s[key]: 
                txt.writelines(line)


def change_cont():
    with open('phone.txt','r', encoding='utf-8') as text:
        s = text.readlines() 
    key = int(input("Введите id контакта для изменения: "))
    key2 = (input("Введите измененный контакт полностью: ")) 
    with open('phone.txt','w', encoding='utf-8') as txt:
        for line in s:
            if line in s[key]: line = key2 
            txt.writelines(line + '\n')


        
        
            
        
        
print('выберите действие:\n'
      +'1 - Вывести справочник на экран\n'
      +"2 - Найти контакт по ключевому слову\n"
      +"3 - Добавить контакт\n"
      +"4 - Удалить контакт\n"
      +"5 - Изменить контакт\n")
num = input()
if num == '1': print_phone()
if num == '2': import_phone()
if num == '3': export()
if num == '4': delete_cont()
if num == '5': change_cont()

