def arg_name(*args):
    names_key = {}
    for i in sorted(args):
        vocabulary = i[0]
        if vocabulary not in names_key:
            names_key[vocabulary] = [i]
        else:
            names_key[vocabulary] += [i]
    
    return names_key

print(arg_name("Иван", "Мария", "Петр", "Илья", " Марина", "Алина", "Бибочка"))