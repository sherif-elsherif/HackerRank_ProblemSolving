#!/bin/python3
# Solution to Extra Long Factoria Problem on HackerRank
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input())

    f = extraLongFactorials(n)
    print(f)
