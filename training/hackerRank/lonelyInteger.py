def lonely_integer(a):
    result = 0
    for num in a:
        result ^= num
    return result


print(lonely_integer([1, 1, 3, 3, 4, 5, 5]))