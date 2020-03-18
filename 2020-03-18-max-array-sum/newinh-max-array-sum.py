#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 1:
        return max(arr[0], 0)
    if len(arr) == 2:
        return max(arr[0], arr[1], 0)

    d = [max(arr[0], 0), max(arr[0], arr[1], 0)]
    
    for i in range(2, len(arr)):
        d.append(max(d[i-1], d[i-2] + arr[i], d[i-2]))

    return d[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
