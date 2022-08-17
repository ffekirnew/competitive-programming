#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    def print_list(list):
        for item in list:
            print(item, end=" ")
        print()
        
    target = arr[-1]
    for index, num in reversed(list(enumerate(arr))):
        if num == target:
            continue
        elif num > target:
            arr[index + 1] = num
            print_list(arr)
        else:
            arr[index + 1] = target
            print_list(arr)
            break
    if target not in arr:
        arr[0] = target
        print_list(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)