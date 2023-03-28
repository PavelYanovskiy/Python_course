# Задача 35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def is_simple(number):
    dividers = []
    for i in range(2, number):
        if number % i == 0:
            dividers.append(i)
    if len(dividers) != 0:
        return dividers
    else:
        return 'yes'


print(is_simple(5))

def simple(n): #создаем фукнцию

    for i in range(2,n): #
        if n % i == 0: # если остаток от деления на числа равно 0
            return "no" #
    return "yes" # 

n = int(input("Введите число: "))
print(simple(n))





def prime(n):
    i = 2
    flag = True
    while i < n and flag: # расскажите про метод флажка
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'yes'
    return 'no'

n = int(input())
print(prime(n))