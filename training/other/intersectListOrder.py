def find_common_elements(list1, list2):
    set1 = set(list1)
    common_set = set1.intersection(list2)
    common_list = [item for item in list1 if item in common_set]
    return common_list


lista1 = [8, 1, 2, 3, 4, 5, 6, 7, 1]
lista2 = [1, 9, 3, 4, 5, 6, 1, 2, 5]

print("common numbers: ",
      find_common_elements(lista1, lista2))

bookshelf1 = ["Harry Potter", "Lord of the Rings", "1984", "Pride and Prejudice", "The Hobbit"]
bookshelf2 = ["Pride and Prejudice", "The Hobbit", "To Kill a Mockingbird", "1984"]

common_books = find_common_elements(bookshelf1, bookshelf2)
print("Common Books:", common_books)