def count_list(lista):
    if not lista:
        return 0
    return 1 + count_list(lista[1:])


print(count_list([1, 2, 3, 4, 5, 6]))
