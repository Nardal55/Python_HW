def multiples_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]

print(multiples_list(int(input("Введите число: "))))