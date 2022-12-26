def decimal_binary(num: int):
    array_num = []

    while num > 0:
        array_num.insert(0, num % 2)
        num //= 2
    print(*array_num, sep="")
decimal_binary(int(input("Введите десятичное число: ")))