'''
Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом 6
'''

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list[2] = 15
del num_list[6]
print(num_list)
