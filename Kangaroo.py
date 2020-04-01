# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen


import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    i = 0
    while i < 1000:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "Yes"
        i += 1
    return "No"



x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)

print(result + '\n')

