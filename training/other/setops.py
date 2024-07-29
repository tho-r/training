
list = [1, 2, 3, 3, 4, 5, 6]
set1 = {1, 3, 5, 7, 9}

# une os 2 sets
unionSet = set1 | set(list)

# intersecçao entre 2 sets
interSet = set1 & set(list)

#diferenças entre os 2 sets
difSet = set1 - set(list)
difSet2 = set(list) - set1

#XOR = itens que só existem em um ou outro set
xorSet = set(list) ^ set1

set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = {2, 3, 5}
print(set3.issubset(set2))
print(set2.issuperset(set3))

print(unionSet)
print(interSet)
print(difSet)
print(difSet2)
print(xorSet)