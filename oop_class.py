# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:17:46 2018

@author: RICHKINWE
"""

class Coordinate(object):
    def __init__(self,x,y):
         self.x=x
         self.y=y
    def dist(self,other):
        p=(self.x-other.x)**2
        q=(self.y-other.y)**2
        return(p+q)**0.5
    def __str__(self):
        return('<',self.x,',',self.y,'>')
    def __add__(self, other):
        return(self.x + other.x, self.y + other.x)
e=Coordinate(9,5)
f=Coordinate(0,0)
print(e.x)
print(Coordinate.dist(e,f))