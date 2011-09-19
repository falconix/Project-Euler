#!/usr/bin/env python
# -*- coding: utf-8 -*-
li=[]
a, b = 1, 1
while b < 4000000:
    if b%2 is 0:
        li += [b]
        a, b = b, a+b

print sum(li)