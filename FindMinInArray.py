#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:01:37 2020

@author: mhimanshu
"""
import math


kidarayBig=[21,6,9,122,4,45,35,3,234,23,23,3345,33,]

min = math.inf

for x in kidarayBig:
    if min > x:
        min = x

print(min)
    
        