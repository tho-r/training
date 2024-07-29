import math
import os
import random
import re
import sys


def plusminus(arr):
    # Write your code here
    zero = pos = neg = 0
    tamanho = len(arr)
    for i in range(tamanho):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1
    print("%.6f" % (pos / tamanho))
    print("%.6f" % (neg / tamanho))
    print("%.6f" % (zero / tamanho))


n = 6
lista = [1, -4, 3, -9, 0, 4]

plusminus(lista)
