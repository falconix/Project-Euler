#!/usr/bin/env python
# -*- coding: utf-8 -*-
value=1000
y=0
z=0
sum_y=0
sum_z=0
li=[]
for x in range(value):
    y=x*5
    if y<value:
        li += [y]
        z=x*3
        if z<value:
            li += [z]

li = set(li)
print sum(li)