# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt #загружаем библиотеку и выгружаем из нее нужную функцию квадратного корня числа
s = int(input("Введите сумму загаданных чисел: ")) #просим ввести сумму чисел
p = int(input("Введите произведение загаданных чисел: ")) #просим ввести произведение чисел
z = sqrt((s/2)**2 - p) #считаем квадратный корень из суммы деленной на 2, возведенной в степень два миинус произведение чисел с
print(int(s/2 - z), int(s/2 + z)) #выводим результатом два числа