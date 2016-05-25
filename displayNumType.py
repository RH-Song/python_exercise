#!/usr/bin/env python
# coding=utf-8
def displayNumType(num):
    print num, 'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type: ', type(num).__name__
    else:
        print 'not a number at all!!'


displayNumType(-69)
displayNumType('xxx')
