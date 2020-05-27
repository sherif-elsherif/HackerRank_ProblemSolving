#!/bin/python3
# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen




def appendAndDelete(s, t, k):
    if abs(len(s)-len(t)) > k:
        return 'No'



s = input()

t = input()

k = int(input())

result = appendAndDelete(s, t, k)

print(result)


