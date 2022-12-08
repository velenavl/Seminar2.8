# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# А) Реализовать создание списка случайных элементов


# Б) Реализовать создание списка случайных элементов - строк

# import datetime

# a = datetime.datetime.now()
# print(a)
# a = str(a)
# print(a)  # покажет время сейчас до милисекунд


# import datetime
# a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds() # (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0) - разница между сегодня и первыми годом, месяцем, днем, часом и секундой, чтобы получить милисекунды
# # print(a)
# a = a%1 # чтобы отбросить целую часть
# print(round(a,6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# # print(a)
# a = a%1
# print(round(a,6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# # print(a)
# a = a%1
# print(round(a,6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# # print(a)
# a = a%1
# print(round(a,6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# # print(a)
# a = a%1
# print(round(a,6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# # print(a)
# a = a%1
# print(round(a,6))


#вариант А - Реализовать создание списка случайных элементов
import datetime
# b1 = 10
# b2 = 20
# a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# a = a%1
# new = round(b1+(b2-b1)*a)
# print(new)

#вариант Б - Реализовать создание списка случайных элементов - строк
# mas = list(map(chr, range(97, 123))) # map - это функция, которая преврачает цифры в нужный формат
# print(mas)
# n = 15
# b1 = 0
# b2 = 25
# a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# a = a%1
# s = ''
# for i in range (10):
#     a = a*(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
#     a = (a*1000)%1
#     print(a)
#     stroka = mas[round(b1+(b2-b1)*a)]
#     s+=stroka
# print(s)

#от преподавателя
import datetime

f=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()

f=int(f)
#print(f)

def myrandint(  start,end,seed=999999999   ):
    a = 32310901 # Сгенерированное случайное число является наиболее равномерным
    b=1729
    rOld=seed
    m=end-start
    while True: # Каждый раз, когда вызывается эта функция myrandint, случайное число генерируется один раз
        rNew = start + (a*rOld+b)%m
        yield rNew
        rOld=rNew
        
 # Симулировать, используя 20 различных семян для генерации случайных чисел
for i in range(5):
    r = myrandint(1,100, f + i)
         # Генерировать 10 случайных чисел на семя
    print ('Seed', i, 'Generate Random Number')
    for j in range(2):
        print( next(r),end=',' )
    print(      )