# Задача 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# a = [1, 1, 2, 0, -1, 3, 4, 4]
# b = set()
# for i in range(len(a)): 
#     b.add(a[i])
# print(len(b))

mass = input().split(", ") #просим пользователя ввести цифры через запятую
new_mass = [] #создаем пустой список
for i in mass:
    if i not in new_mass:
        new_mass.append(i)
count = len(new_mass)
print(count)