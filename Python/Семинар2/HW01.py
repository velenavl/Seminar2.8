# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')

# sum = 0
# input_num = input('Введите число: ')

# for a in input_num:
#     if a.isdigit():
#         sum += int(a)

# print(sum)