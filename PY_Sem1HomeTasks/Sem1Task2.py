# Задача 2: Найдите сумму цифр трехзначного числа

#1 вариант решения задачи
n = int(input("Введите число: ")) # предлагаем пользователю ввести число
a = n // 100 #выводим первое число поделив на 100
b = n // 10 % 10 #выводим 2 число разделив на 10 и получив остаток от деления на 10
c = n % 10 #выводим 3 число из остатка от деления на 10
print("Сумма цифр числа: ", a + b + c)


# 2 вариант решения
# n = int(input("Введите число: "))
# digit1 = n % 10 #отстаток от деления на 10 извлекаем цифры
# n = n // 10
# digit2 = n % 10
# n = n // 10
# print("Сумма цифр числа: ", n + digit1 + digit2) #складываем все получившиеся числа



# 3 вариант решения
# n = int(input("Введите число: "))
# sum_of_digits = 0
# while n > 0:
#     digit = n % 10
#     sum_of_digits += digit
#     n //= 10

# print("Сумма цифр числа:", sum_of_digits)