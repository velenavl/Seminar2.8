from fileinput import close
from importlib.resources import path
from turtle import color




# color = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# # data.writelines(color)
# data.write('Line1\n')
# data.write('Line2\n')
# data.close() #для закрытия

# 2 способ
# with open('file.txt', 'a') as data:
#    data.write('Line 12\n')
#    data.write('Line 13\n') 

# открытие для чтения данных
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Импортировать из другого файла функцию
# import hello as h
# print(h.f(1))

# Функции
# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# Возможность передачи неограниченного количества аргументов
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2)) # TypeError: can only concatenate str (not "int") to str

# если числа
# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4)) # 10


# Функция. Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34




# Кортежи - неизменяемые списки
# a = (3, 1, 41, 4)
# print(a)
# print(a[-1]) # покажет последний элемент
# print(a[-2]) # покажет предпоследний элемент
# print(a[1])
# print(a[0])

# for item in a: # кортеж через for
#     print(item)

# #Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '→',
#         'down': '↓',
#         'right': '→'
#     }
# # print(dictionary)
# # print(dictionary['left'])

# # выдать ключи
# # for k in dictionary.keys():
# #     print(k)

# # выдать значения
# for k in dictionary.values():
#     print(k)


# Множества
# colors = {'red', 'green', 'blue'} 
# print(colors)
# # colors.add('gray')
# # print(colors)
# # colors.remove('red')
# # print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a)