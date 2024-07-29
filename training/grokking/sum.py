def soma(lista):
    if not lista:
        return 0
    return lista[0] + soma(lista[1:])


print(soma([1, 2, 3, 4, 5, 6, 6, 2, 1, 1]))



