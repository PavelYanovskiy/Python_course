# Задача №37. 
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def f(n):
    if n == 0: #если н = 0
        return '+' #то мы возвращаем пустую строку или плюсик
    k = int(input())  #каждый раз вводим число в консоль
    return f(n - 1) + f' {k}' #послений элмент будет пустая строка + фкэ


n = int(input()) #вводим числа
print(f(n)) #функция ф от н



def reverse(a): #
    if len(a) == 0:  #если длина 
        return ""
    else: 
        return str(reverse(a[1:])) + a[0]

n = input("Введите последовательность: ")
print(reverse(n))