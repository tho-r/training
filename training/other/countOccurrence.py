def contadorlista(lista):
    dihct = {}

    for i in lista:
        if i in dihct:
            dihct[i] += 1
        else:
            dihct[i] = 1

    return dihct


print(contadorlista([1, 2, 2, 3, 9, 0, 2, 3, 2, 2, 2, 00, 1]))
