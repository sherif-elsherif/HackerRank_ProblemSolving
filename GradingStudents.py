# https://www.hackerrank.com/challenges/grading/problem


def grade_students(alist):
    i = 0
    while i < len((alist)):
        x = alist[i] % 5
        x = 5 - x
        if x >= 3:
            i +=1
            continue

        if (alist[i] + x) < 40:
            i += 1
            continue # do nothing
        elif (alist[i] + x) > 100:
            alist[i] = 100
        else:
            alist[i] = alist[i] + x
        i += 1
    print('\n'.join(map(str, result)))


n = int(input())
grades = []
i = 0
while i < n:
    grades.append(int(input()))
    i += 1

grade_students(grades)
