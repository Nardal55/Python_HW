def fib_num(num: int):
    a, b = 1, 1
    list_num = [0]

    for i in range(num):
        list_num.append(a)
        list_num.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return list_num
print(*fib_num(int(input("Введите число: "))))