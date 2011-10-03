#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import operator
number = 600851475143
n=2
li=[]
sqrt_number = int(round(math.sqrt(number)))
for x in range(sqrt_number):
    try:
        if int(reduce(operator.mul, li))==number:
            print n
            break
    except TypeError:
        pass
    if number%n is 0:
        li += [n]   
    n=n+1



