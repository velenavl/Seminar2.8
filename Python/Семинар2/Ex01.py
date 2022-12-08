# Написать программу, которая принимает строку и букву и определяет индексы первого и последнего вхождения буквы в строке
from tracemalloc import start


# str1 = input('Введите строку: ')
# str2 = input('Введите букву: ')

# start = -1
# stop = -1

# for i in range(len(str1)):
#     if str1[i] == str2:
#         stop = i
#         if start == -1:
#             start = i

# print(start+1)
# print(stop+1)


# 2 вариант

str1 = input('Введите строку: ')
str2 = input('Введите букву: ')

start = None
stop = None

for i in range(len(str1)):
    if str1[i] == str2:
        stop = i
        if start == None:
            start = i

print(start+1)
print(stop+1)