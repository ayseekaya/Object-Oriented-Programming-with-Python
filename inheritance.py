# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 00:12:32 2022

@author: ayyse
"""
#parent
class Animal:
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")
        

#child
class Monkey(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("monkey is created")
    
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
        

#child
class Bird(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("bird is created")
        
    def fly(self):
        print("bird can fly")
        
m1=Monkey()
m1.toString()
m1.walk()
m1.climb()

b1=Bird()
b1.toString()
b1.fly()
b1.walk()


