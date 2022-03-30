# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
integer1=5
string1="okdodkw"
# %%


class Employee(object):
    #attribute: age,eye
    #behaviour:run,pass
    pass
employee1=Employee() #object is created


# %%

class Footballer:
    football_club="Barcelona"
    age=30
    
f1=Footballer()
print(f1.age,f1.football_club)

f1.football_club="real madrid"
print(f1.age,f1.football_club)


# %%
class Square(object):
    edge=5
    area=0
    def area1(self):
        self.area=self.edge*self.edge
        print("Area: ",self.area)
        
        
s1=Square()   
print(s1.area1())


s1.edge=7
s1.area1()

# %% methods vs functions
#method sınıfa bağımlı, sınıf içinde tanımlanıyor, 
#fonksiyon bağımsız sınıf dışında tanımlanır
class Emp(object):
    age=50
    salary=2000
    
    def agesalaryRatio(self):
        a=self.age/self.salary
        print("method: ",a)
        
e1=Emp()
e1.agesalaryRatio()

def agesalaryRatio(age,salary):
    a=age/salary
    print("function: ",a)
    
agesalaryRatio(50, 6000)


def findarea(pi,r):
    area=pi*r**2
    #print(area)
    return area
    
pi=3.14
r=10
findarea(pi, r)

result1=findarea(pi, 5)
result2=findarea(pi, r)
print(result1+result2)


class Animal(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getAge(self):
        return self.age
    def getName(self):
        print(self.name)
        
a1=Animal("Dog",2)
a2=Animal("lion",3)
a3=Animal("cat",4)
a3.getName()







































































