quarter_num = int(input('Введите номер четверти: '))

if quarter_num == 1:
    print('В первой четверти -> x > 0 y > 0')
elif quarter_num == 2:
    print('Во второй четверти -> x < 0 y > 0')
elif quarter_num == 3:
    print('В третьей четверти -> x < 0 y < 0')
elif quarter_num == 4:
    print('В четвертой четверти -> x > 0 y < 0')
else:
    print('Такая четверть отсутствует')