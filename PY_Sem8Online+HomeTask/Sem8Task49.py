# Задача №49.
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
# не должна быть линейной

#Решеие с семинара
# def show_menu() -> int:
#     print("\nВыберите необходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. Найти абонента по фамилии\n"
#           "3. Найти абонента по номеру телефона\n"
#           "4. Добавить абонента в справочник\n"
#           "5. Сохранить справочник в текстовом формате\n"
#           "6. Закончить работу")
#     choice = int(input())
#     return choice



# # def read_csv(filename: str) -> list:
# #     data = []
# #     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
# #     with open(filename, 'r', encoding='utf-8') as fin:
# #         for line in fin:
# #             record = dict(zip(fields, line.strip().split(',')))
# #             data.append(record)

# #     return data
# import csv

# def display_all_records():
#             for row in reader:
#                 print(*row)

# def find_last_name():
#      last_name = input('Введите фамилию: ')
#      for elem in filter(lambda x: x[0] == last_name, reader):
#           print(f'Фамилия: {elem[0]}\nИмя: {elem[1]}\nНомер телефона: {elem[2]}\nКомментарий: {elem[3]}\n')
     
# def find_phone_number():
#      phone = input('Введите телефон ')
#      return filter(lambda x: x[2] == phone, reader)

# def add_abonent():
#      with open('phonebook.csv', 'a', encoding='utf-8', newline='') as out_file:
#           info = input('Введите данные абонента: ').split()
#           csv.writer(out_file).writerow(info)


# for elem in iter(input, '6'):
#     with open('phonebook.csv', 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)

#         if elem == '1':
#             display_all_records()

#         if elem == '2':
#             find_last_name(reader)

#         if elem == '3':
#             print(find_phone_number(reader))

import csv

def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open('phonebook.txt', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([name, surname, patronymic, phone_number])
    print("Контакт успешно добавлен")

def search_contact():
    search_term = input("Введите имя, фамилию или отчество для поиска: ")
    with open('phonebook.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if search_term in row:
                print(row)

def export_contacts():
    with open('phonebook.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        with open('exported_phonebook.txt', mode='w', newline='') as export_file:
            writer = csv.writer(export_file, delimiter=',')
            for row in reader:
                writer.writerow(row)
    print("Контакты успешно экспортированы")

def edit_contact():
    search_term = input("Введите имя или фамилию контакта для редактирования: ")
    with open('phonebook.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)
        for i, row in enumerate(rows):
            if search_term in row:
                print(f"Контакт найден: {row}")
                new_name = input("Введите новое имя: ")
                new_surname = input("Введите новую фамилию: ")
                new_patronymic = input("Введите новое отчество: ")
                new_phone_number = input("Введите новый номер телефона: ")
                rows[i] = [new_name, new_surname, new_patronymic, new_phone_number]
                with open('phonebook.txt', mode='w', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerows(rows)
                print("Контакт успешно изменен")
                return
        print("Контакт не найден")

def delete_contact():
    search_term = input("Введите имя или фамилию контакта для удаления: ")
    with open('phonebook.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)
        for i, row in enumerate(rows):
            if search_term in row:
                print(f"Контакт найден: {row}")
                del rows[i]
                with open('phonebook.txt', mode='w', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerows(rows)
                print("Контакт успешно удален")
                return
        print("Контакт не найден")

while True:
    print("Выберите действие:")
    print("1. Добавить контакт")
    print("2. Поиск контакта")
    print("3. Экспорт контактов")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выход")
    choice = input("Введите номер действия: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        export_contacts()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Неверный выбор")
