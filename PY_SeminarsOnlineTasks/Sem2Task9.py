# Задача 9 По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

n = int(input('Введите неотрицательное число '))
if n == 0: #если введеное число равно 0 то печатаем 1
    print('1')
factorial = 1 #рассчитываем факториал 1ы
while n:
    factorial *= n #факториал умножить либо равно н
    n-=1
print(factorial)