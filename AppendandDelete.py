#!/bin/python3
# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen

"""
abcd
abcdert
10
"""
def appendAndDelete(s, t, k):
    if abs(len(s)-len(t)) > k:
        return 'No'
    matched_string = ''
    min_len = min(len(s), len(t))
    for i in range(min_len):
        if s[i] == t[i]:
            matched_string = t[0:i+1]
            continue
        else:
            matched_string = t[0:i]
            break
    print(matched_string)

    if len(t) > len(s) and len(t)-len(matched_string)+len(s)-len(matched_string) > k:
        return 'No'
    elif len(t) < len(s) and len(s)-len(matched_string)+len(t)-len(matched_string) > k:
        return 'No'
    elif len(t) == len(s) and len(s)-len(matched_string)+len(t)-len(matched_string) > k:
        return 'No'
    else:
        return 'Yes'



s = input()

t = input()

k = int(input())

result = appendAndDelete(s, t, k)

print(result)


