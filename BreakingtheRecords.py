# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


import os

# Complete the breakingRecords function below.
def breakingRecords(scores):
    i = 1
    max_score = min_score = scores[0]
    records = [0, 0]
    max_count = min_count = 0

    while i < len(scores):
        if scores[i] > max_score:
            max_score = scores[i]
            records[0] += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            records[1] += 1
        i += 1
    return records

n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(' '.join(map(str, result)))
