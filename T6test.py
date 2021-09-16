#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:03:32 2020

@author: mhimanshu


"""
mathop=input("Siri :enter any option +,*,-  :")

User1Number=input("Siri :write your first number :")
User2Number=input("Siri :write your secend number :")

f = int(User1Number)
t = int (User2Number)

if mathop=='*':
    print("maltipliction:",f*t)
elif mathop=='+':    
    print("sum:",f+t)
elif mathop=='-':    
    print("subrection:",f-t)
else:
    print("you entered wrong option")





    
