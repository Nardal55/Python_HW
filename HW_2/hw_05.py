from random import randrange

num = int(input())
num_list = list(range(num))
array_res = []
print(num_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    num_list[n_1], num_list[n_2] = num_list[n_2], num_list[n_1]

print(num_list)
