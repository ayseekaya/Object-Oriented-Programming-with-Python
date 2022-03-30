# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:45:18 2022

@author: ayyse
"""

class Calc(object):
    "calculator"
    def __init__(self,a,b):
        "initialize values"
        self.value1=a
        self.value2=b
    
    def Add(self):
        "addition a+b =result ->return result"
        return self.value1+self.value2
    def Multiply(self):
        "multiplication a*b =result ->return result"
        return self.value1*self.value2
    def Division(self):
        "division a/b =result ->return result"
        return self.value1/self.value2
    
print("choose add(1), multiply(2), division(3)")
selection=input("select 1 or select 2 or select 3 ") 
  
v1=int(input("first value "))
v2=int(input("second value "))
c1=Calc(v1,v2)

if selection=="1":
    add_result=c1.Add()
    print("Add: {}".format(add_result))
elif selection=="2":
    multiply_result=c1.Multiply()
    print("Multiply: {}".format(multiply_result))
elif selection=="3":
    division_result=c1.Division()
    print("Division: {}".format(division_result))
else:
    print("Error there is no proper selection")


























