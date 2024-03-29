from itertools import groupby, starmap
from os import path

def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
            else:
                print("Укажите верно")

def rle_decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_num = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_num.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_num)))
    else:
        print("Нет файла в системе")

rle_encode(input("Введите имя файла с текстом: "), input("Введите файл для записи: "))
rle_decode(input("Введите файл для декодирования: "))