# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:                Ввод:
# 5                    5
# 1 2 3 4 5            1 5 1 5 1
# Вывод:               Вывод:
# 0                    2
#                     (каждое число вводится с новой строки)

from random import randint as RD
n = int(input("Введите количество элементов в первом массиве: "))

list = [RD(1, 10) for _ in range(n)] #если переменная не нужна, можно использовать знак подчеркивания

print(list)
count = 0
index = []
for i in range(1, len(list) - 1):
    if list[i-1] < list[i] > list[i]:  # if list[i-1] < list[i] and list[i+1] < list[i]:
        count += 1
        index.append(i)
print(f"Индексы чисел массива:{index}")
print(count)