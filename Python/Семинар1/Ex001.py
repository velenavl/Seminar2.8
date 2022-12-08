# Программа принимает на вход 2 числа и проверяет, является ли одно число квадратом второго

a = int(input('Введите а: '))
b = int(input('Введите b: '))
if a == b * b:
    print('Да')
elif b == a * a:
    print('Да')
else:
    print('Нет')

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# if(a == b * b) or (b == a * a):
#     print('Да')
# else:
#     print('Нет')