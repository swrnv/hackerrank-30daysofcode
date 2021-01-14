import math
import os
import random
import re
import sys



if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))



total = 0
max_total = -1073741824


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (j+2 < 6) and (i+2 < 6):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if max_total < total:

                max_total = total
print(max_total)
