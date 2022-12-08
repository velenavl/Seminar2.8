# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:


# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
list_in = [int(i) for i in input("введите посследовательность: ").split()]
list_out = []

len_count = len(list_in)
len_count = int(len_count/2) + len_count%2


for i in range(len_count): 
    list_out.append(list_in[i]*list_in[i*-1-1])
print (list_out)