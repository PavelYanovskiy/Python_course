# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


from random import randint

def change_marks(line_1):
    min_mark = min(line_1)
    max_mark = max(line_1)
    for i in range(len(line_1)):
        if line_1[i] == max_mark:
            line_1[i] = min_mark
    return line_1

n = int(input("Общее число оценок: "))
line_1 = [randint(1, 5) for i in range(n)]
print(*line_1)
print(*change_marks(line_1))