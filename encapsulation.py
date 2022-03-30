# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:05:11 2022

@author: ayyse
"""

#encapsulation: sınıflara doğrudan erişimi engellemek için kullanılır
class BankAccount(object):
    def __init__(self,name,money,address):
        self.name=name
        self.__money=money #private
        self.address=address
        
    def getMoney(self):
        return self.__money
    
    def setMoney(self,amount):
        self.__money=amount
        
        
     #private    
    def __increase(self): 
        self.__money=self.__money+500
        
p1=BankAccount("messi", 5000, "barcelona")
p2=BankAccount("neymar", 2000, "paris")

print("get method: ",p1.getMoney())

p1.setMoney(6000)
print("after set method:",p1.getMoney())

# p1.increase()
# print("after increase:",p1.getMoney())
