
#LINK https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    sum_right = 0
    count_r = 0
    sum_left = 0
    count_l = len(arr)-1
    
    for x in range(len(arr)):
        sum_right += arr[x][count_r]
        sum_left += arr[x][count_l]
        count_r +=1
        count_l -=1

    return abs(sum_right-sum_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
