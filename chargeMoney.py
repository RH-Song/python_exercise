#!/usr/bin/env python
# coding=utf-8

def chrageMoney(totalMoney):
    count = 0
    count += totalMoney/25
    left = totalMoney%25
    count += left/10
    left = left%10
    count += left/5
    left = left%5
    count += left/1
    return count

# better way to do
def chrageMoney2(totalMoney):
    left = totalMoney
    count = 0
    chrage = [25,10,5,1]
    for c in chrage:
        count += left/c
        left = left%c
    return count


print chrageMoney(76)
print chrageMoney2(76)
