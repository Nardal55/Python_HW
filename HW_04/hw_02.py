num = int(input("Введите число: "))
i = 2 
array = []
corrected = num
while i <= num:
    if num % i == 0:
        array.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Множители числа {corrected} -> {array}")