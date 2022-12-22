num = int(input("Сколько чисел: "))
sum_num = 0
array_num = []
for n in range(1, num + 1):
    result = round((1 + 1 / n) ** n, 3)
    array_num.append(result)
    sum_num += result
print(array_num)
print(sum_num)