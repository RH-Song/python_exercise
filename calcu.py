#!/usr/bin/env python
# coding=utf-8

def cal(s):
    result = 0
    [a , c, b] = s.split(' ')
    num1 = int(a)
    num2 = int(b)
    if c == '+':
        result = num1+num2
    elif c == '-':
        result = num1-num2
    elif c == '*':
        result = num1 * num2
    elif c == '/':
        result = num1 /num2
    elif c == '**':
        result = num1 ** num2
    return result

s = raw_input()
print cal(s)
