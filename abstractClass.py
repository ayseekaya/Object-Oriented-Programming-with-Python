# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:11:29 2022

@author: ayyse
"""
#abstract classlar subclasslar için şablon görevi görürler ve nesne yaratılamaz
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self): pass

    
    def run(self): pass

    
class Bird(Animal):
    
    def __init__(self):
        print("bird")
        
    def walk(self):
        print("walk")
        
b1=Bird()
b1.run()
b1.walk()