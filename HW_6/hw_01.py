from random import sample

array_list = int(input("Введите число для формирования списка: "))
my_array = [i for i in sample(range(1, array_list * 2), array_list)]
print(my_array)
sort_array = [my_array[i]
             for i in range(1, len(my_array)) if my_array[i] > my_array[i-1]]
print(sort_array)