num = int(input("Введите число: "))
sum_digits = 1
num_list = []
for n in range(num):
    sum_digits *= n + 1
    num_list.append(sum_digits)
print(num_list)
