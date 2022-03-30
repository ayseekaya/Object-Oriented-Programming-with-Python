# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:37:59 2022

@author: ayyse
"""

class Animal:
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    def toString(self):
        print("monkey")
        
a1=Animal()
a1.toString()

m1=Monkey()
m1.toString()