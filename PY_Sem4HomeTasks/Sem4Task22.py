# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: ")) #просим ввести количество переменных в каждом из двух множеств
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

for i in range(n):
    set1.add(int(input("Введите элемент первого множества: ")))

for i in range(m):
    set2.add(int(input("Введите элемент второго множества: ")))

result_set = set1.intersection(set2) #находим пересечения множеств и выдаем результат в отсорированном порядке
result_list = sorted(list(result_set))

print("Результат: ", result_list)
