#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:22:46 2020

@author: mhimanshu
"""
isContinue = "y"

while(isContinue == "y"):
    x=input("Siri :enter your first number:")
    y=input("Siri :enter your second number:")

    if x<y:
        print("greater number:",y)
    elif x==y:
        print("both are equal:",x,y)
    else:
        print("greater number:",x)
        
    isContinue=input("Siri :do you want to continue y/n:")

print("you ended the programf")