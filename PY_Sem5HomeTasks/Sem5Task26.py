# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 



def pow(a, b): #назначаем функцию и назначаем переменные
    if b == 0: #прописываем базис рекурсии. Если степень равна 0, то функция возвращает 1.
        return 1 #возвращаем 1
    return a * pow(a, b-1) #функция вызывает саму себя с числом `a` в степени `b-1` и умножает результат на `a`


a=int(input('Введите число: ')) #просим пользователя ввести число
b=int(input('Введите степень: ')) #просим пользователя ввести стпень, в которую нужно возвести число

result = pow(a, b)

print(f"ЧИсло {a} в степени {b} равно {result}") #вывыодим пользователю итог
