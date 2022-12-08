# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой
from itertools import count


# str1 = input('Введите первую строку: ')
# str2 = input('Введите вторую строку: ')

# count = 0

# for i in range(len(str1)-2):
#     if str1[i:i+len(str2)] == str2:
#         count = count + 1
# print("n = ", count)

a=input()
b=input()
c=a.count(b)
print(c)
