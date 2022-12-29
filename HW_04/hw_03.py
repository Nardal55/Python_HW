from random import randint


num = int(input("Введите число: "))
array = []        
for i in range(1,num + 1):
    num2 = randint(1,10)
    array.append(num2)
print(array)


new_array = []
for i in array:
    if i not in new_array:
        new_array.append(i)

print(new_array)


# не понятно как тут коллекшн применять( и парные к меня все равно пишутся в new_array)