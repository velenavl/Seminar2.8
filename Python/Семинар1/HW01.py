# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
# print('Введите цифру, обозначающую день недели: ')
# dayNamber = int(input())
# if (dayNamber == 6) or (dayNamber == 7):
#     print('Это выходной день')
# elif (dayNamber >= 8) or (dayNamber <= 0):
#     print('Ошибка')
# else:
#     print('Это не выходной день')


# *Напишите программу, которая принимает на вход 2 числа: номер месяца и номер дня в месяце, проверяет является ли день выходным.
# Принимаем начало года на понедельник и считая год не високосным. Учитываем только гос праздники (НГ, 9 мая и т.д.)

print('Введите номер месяца: ')
monthNamber = int(input())
print('Введите номер дня в месяце: ')
dayNamber = int(input())
if (monthNamber == 1) and (dayNamber >= 1 and dayNamber <= 10) or (monthNamber == 2) and (dayNamber == 23) or (monthNamber == 3) and (dayNamber == 8) or (monthNamber == 5) and (dayNamber == 1) or (monthNamber == 5) and (dayNamber == 9) or (monthNamber == 11) and (dayNamber == 4) or (monthNamber == 12) and (dayNamber == 12):
    day_status = "Это государственный праздник"
elif (dayNamber >= 32) or (dayNamber <= 0):
    day_status = "Ошибка"
day = dayNamber
for i in range(6,365,7):
    if i == day:
        day_status = "Это выходной день"
for i in range(7,365,7):
    if i == day:
        day_status = "Это выходной день"
for i in range(1, monthNamber):
    if i == 4 or i == 6 or i == 9 or i == 11:
        day += 30
    elif i == 2:
        day += 28
    else:
        day += 31
        day_status = "Это не выходной день"

print(day_status)




