# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Введите длину шоколадки: ")) # узнаем одну сторону шоколадки
m = int(input("Введите ширину шоколадки: ")) # узнаем другую сторону шоколадки
k = int(input("Введите количество долек, которые хотите отломить: ")) # спрашиваем сколько долек хоти отломить
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Да, можно отломить", k, "долек.")
else:
    print("Нет, нельзя отломить", k, "долек.")