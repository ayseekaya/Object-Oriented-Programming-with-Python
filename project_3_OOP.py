# -*- coding: utf-8 -*-dssddsds
"""
Created on Thu Mar 31 09:19:17 2022

@author: ayyse
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):pass
    
    @abstractmethod
    def perimeter(self):pass
    
    def toString(self):pass
    
    
class Square(Shape):
    
    def __init__(self,edge):
        self.__edge=edge
        
    def area(self):
       result=self.__edge**2
       print("Area:",result)
       
    def perimeter(self):
        result=4*self.__edge
        print("Perimeter: ",result)
        
    def toString(self):
        print("Square edge: ",self.__edge)
        
        
class Circle(Shape):
    PI=3.14
    def __init__(self,radius):
        self.__radius=radius
        
    def area(self):
       result=self.PI*self.__radius**2
       print("Area:",result)
       
    def perimeter(self):
        result=self.PI*2*self.__radius
        print("Perimeter: ",result)
        
    def toString(self):
        print("Circle radius: ",self.__radius)
        
        
s1=Square(5)
s1.area()
s1.perimeter()
s1.toString()


c1=Circle(5)
c1.area()
c1.perimeter()
c1.toString()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        