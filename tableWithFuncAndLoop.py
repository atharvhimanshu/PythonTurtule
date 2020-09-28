#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:08:04 2020

@author: mhimanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:34:48 2020

@author: mhimanshu
"""
def table(t):
    for x in range(11):
        if x==0:
            print("")
        else:
            print(t,"x",x,"=",x*t)

#print(x)            

#table(9)

for y in range(4):
    if y==0:
          print("")
    else:      
      table(y)

print("------------")   
   
for y in range(4):
    if y>0:
        table(y)  

print("*************")   
     
for y in range(4):
        table(y+1)     