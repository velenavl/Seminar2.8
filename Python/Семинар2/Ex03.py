# Получить список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200. Выполнить только при первом вхождении числа 20.
# N = int(input('Введите число N: '))
# import random


# N = 20

# list1 = []
# for i in range(N):
#     list1.append(random.randint(0, 50))
# print(list1)

# for i in range(len(list1)):
#     if list1[i] == 20:
#         list1[i] = 200
#         break
# print(list1)



N = 10

list1 = []
for i in range(N):
    list1.append(int(input(f'Введите {i} число массива: ')))
print(list1)

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)
