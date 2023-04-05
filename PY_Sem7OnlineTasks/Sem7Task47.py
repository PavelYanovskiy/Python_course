# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Задача №47. Решение в группах
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

values = [1, 23, 42, 'asdfg'] #
transformed_values = list(map(lambda x: x, values)) # создаем список в котором для каждого значения этого списка применяется такое значение, 
#попросту копируем список по элементам и возвращаем его. для каждого эоемента списка возвращает сама себя

print(values)
print(transformed_values)

if values == transformed_values:
 print('ok')
else:
 print('fail')
