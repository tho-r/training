#remover duplicatas de uma lista transformando ela em um set, e retornando como uma lista
def remove_duplicates(my_list):
    return list(set(my_list))


x = [2, 1, 3, 2, 2, 4, 5, 6, 7, 8]
print(remove_duplicates(x))


#fazer a mesma coisa, porem mantendo a ordem original da lista
def remove_dupe_ordered(my_list):
    return list(dict.fromkeys(my_list))


print(remove_dupe_ordered(x))
