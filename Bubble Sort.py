#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numSwaps = 0

    numSwaps = 0
    exchanges = True

    while exchanges:
        exchanges = False
        for pass_num in range(len(a) - 1, 0, -1):
            for i in range(pass_num):
                if a[i] > a[i + 1]:
                    temp = a[i]
                    a[i] = a[i + 1]
                    a[i + 1] = temp
                    numSwaps += 1
                    exchanges = True

    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)