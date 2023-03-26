# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# text = input().split() #берется строка, делаится насимвоолы
# a = {} #создаем пустой словарь
# for i in text: #проходимся по этой строке списка
#     if i not in a:  #если элемент списка отсутсвует в словаре, добавляем в значение 1
#         a.update({i:1}) #update добавить словарь в элемент
#     else:
#         a[i] += 1  #значение в словаре увеличиваем на 1
#     print(f"{i}_{a[i]}", end=" ")


# sp = input("Введите строку: ").split()
# result = {} #завели словарь
# for i in sp:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
# result[i] = result.get(i, 0) + 1

string = input('Введите строку: ').split()
letter_dict = {}
result_string = []
for letter in string:
    if letter in letter_dict.keys():
        result_string.append(f'{letter}_{letter_dict[letter]}')
else:
    result_string.append(letter)
    letter_dict[letter] = letter_dict.get(letter, 0) + 1

print(' '.join(result_string))