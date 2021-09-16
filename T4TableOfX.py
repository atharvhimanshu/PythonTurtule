#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:19:55 2020

@author: mhimanshu
"""

usernumber=input("can I no your number I will write its table:")

r=int(usernumber)


for x in range(11):
    if x==0:
        print("")
    else:
        print(r,"x",x,"=",x*r)
       