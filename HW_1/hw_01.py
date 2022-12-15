number = int(input("Введите число от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели не корректное число')
elif number > 5:
    print('Урааааааа!!! Выходной!')
else:
    print('Печально, это рабочий день!')