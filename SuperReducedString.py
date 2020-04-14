# https://www.hackerrank.com/challenges/reduced-string/problem


import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def superReducedString(s):
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s.replace(s[i],"")
            # s = s.replace(s[i+1],"")
            i = 0
            continue
        i += 1
        return s


s = input()

result = superReducedString(s)

print(result + '\n')