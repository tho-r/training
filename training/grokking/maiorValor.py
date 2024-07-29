def maximun(listao):
    if not listao:
        return 0
    if len(listao) == 2:
        if listao[0] > listao[1]:
            return listao [0]
        elif listao[1] < listao [0]:
            return listao[1]
    sub_max = maximun(listao[1:])
    if listao[0] > sub_max:
        return listao[0]
    else:
        return sub_max


print(maximun([1, 2, 1293, 2, 4, 5000, 5000, 1]))