# Получить список чисел. Превратите его в список квадратов этих чисел.
import random


N = int(input('Введите число N: '))

list1 = []
for i in range(N):
    list1.append(random.randint(15, 21))
print(list1)

for i in range(len(list1)):
   list1[i] = list1[i] * list1[i]
print(list1)