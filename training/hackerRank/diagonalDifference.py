def diag_dif(arr):
    n = 3
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][len(arr)-1-i]
        print(len(arr)-1-i)
    return(abs(d1-d2))


print(diag_dif([[11, 2, 3], [4, 5, 6], [10, 8, -12]]))


x = [[11, 2, 3], [4, 5, 6], [10, 8, -11]]

print(x[1],[2])