# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов

import random

N = int(input('Введите число N: '))
print(f"Для N = {N}: ", end= "")

arr = []
for i in range(N):
    arr.append(random.randint(-100, 100))

print(arr)