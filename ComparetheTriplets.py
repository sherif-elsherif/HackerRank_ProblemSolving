

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    i = 0
    score = [0, 0]
    while i < len(a):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
        i += 1
    return score


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
