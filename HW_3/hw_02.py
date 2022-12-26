from random import sample

def list_rand_nums(count):
    if count < 0:
        print("Введите верное число")
        return[]
    list_num = sample(range(1, count * 2), count)
    return list_num

def num_pairs(list_num: list):
    res_list = []
    len_list = len(list_num)
    for i in range(len_list // 2):
        res_list.append(list_num[i] * list_num[len_list - i - 1])
    if len_list % 2:
        res_list.append(list_num[len_list // 2])
    return res_list

array_list = list_rand_nums(int(input("Введите число: ")))
print(array_list)
print(num_pairs(array_list))

