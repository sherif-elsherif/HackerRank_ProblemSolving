#!/bin/python3
# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen




def appendAndDelete(s, t, k):
    if abs(len(s)-len(t)) > k:
        return 'No'
    matched_string = ''
    for i in range(len(t)):
        if s[i] == t[i]:
            matched_string = t[0:i+1]
            continue
        else:
            matched_string = t[0:i]
            break
    print(matched_string)
    # Check if you can append the missing values
    if len(t)-len(matched_string) > k:
        return 'No'
    else:
        return 'Yes'
    # Start appending the missing values if you'd like to
    t_index = len(matched_string)
    while t_index < len(t):
        matched_string += t[t_index]
        t_index += 1
    return matched_string



s = input()

t = input()

k = int(input())

result = appendAndDelete(s, t, k)

print(result)


