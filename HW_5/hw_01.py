from random import sample

def array_list(count: int, alp: str = 'абв'):
    words_array = []
    for i in range(count):
        letters = sample(alp, k=3)
        words_array.append("".join(letters))
    return " ".join(words_array)

def string_cheak(words: str) -> str:
    return " ".join(i for i in words.split() if i != "абв")

all_array = array_list(int(input("Numbers: ")))
print(all_array)
print(string_cheak(all_array))