#!/usr/bin/env python
# coding=utf-8

def testGrade(grade):
    if 100 >= grade >= 90:
        return 'A'
    elif 90 > grade >= 80:
        return 'B'
    elif 80 > grade >= 70:
        return 'C'
    elif 70 > grade >= 60:
        return 'D'
    elif 60 > grade:
        return 'F'
    else:
        return 'Not a right grade.'

grade = raw_input('Enter your grade: ')
print testGrade(int(grade))
#print testGrade(99)
