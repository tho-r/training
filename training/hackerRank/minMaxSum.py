def minmax(array):
    array.sort()
    mini = array[0]
    maxi = array[-1]
    for i in array[1:-1]:
        mini += i
        maxi += i
    print(mini, maxi)


minmax([1, 3, 5, 7, 9])
