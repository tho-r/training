def counting_sort(arr):
    my_array = [0] * 100
    for i in arr:
        my_array[i] += 1
    return my_array


print(counting_sort([1, 2, 2, 2, 1, 3, 3, 3, 4, 5, 6, 7, 8]))
