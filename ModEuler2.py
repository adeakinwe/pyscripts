# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:47:07 2018

@author: Adeseto, AKINWE
"""
import math
from matplotlib import pyplot as plt
import numpy as np

def ModEul(f,x0,y0,x1,n):
    wx = [0]*(n+1)
    wy = [0]*(n+1)
    h = (x1-x0)/float(n)
    wx[0]= x = x0
    wy[0]= y = y0
    for i in range(1,n+1):
        f1 = f(x,y)
        f2 = f(x + h, y + h*f1)
        wx[i] = x = x0 + i * h
        wy[i] = y = y + (h*(f1+f2))/2.0
    return wx, wy

def f(x, y):
    return x**3+x*y
 
wx, wy = ModEul(f, 0, 1, 1, 5)
for x, y in list(zip(wx, wy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))
    plt.plot(wx, wy,'ro',lw=1, label='Modified-Euler')
    plt.plot(vx, vy,'b-', lw=1, label='Runge-Kutta')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.show()
#=================================================
def ModEul(f,x0,y0,x1,n):
    wx = [0]*(n+1)
    wy = [0]*(n+1)
    h = (x1-x0)/float(n)
    wx[0]= x = x0
    wy[0]= y = y0
    for i in range(1,n+1):
        f1 = f(x,y)
        f2 = f(x + h, y + h*f1)
        wx[i] = x = x0 + i * h
        wy[i] = y = y + (h*(f1+f2))/2.0
    return wx, wy

def f(x, y):
    return y**2-y-2
 
wx, wy = ModEul(f, 0, 1, 1, 5)
for x, y in list(zip(wx, wy))[:]:
    print("%1.2f   %10.16f   %10.16f   %12.4e" % (x, y,(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))), abs(y-(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))))))
    plt.plot(wx, wy,'r-',lw=1, label='Modified-Euler')
    plt.plot(vx, vy,'b-', lw=1, label='Runge-Kutta')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.show()

#==================================
def ModEul(f,x0,y0,x1,n):
    wx = [0]*(n+1)
    wy = [0]*(n+1)
    h = (x1-x0)/float(n)
    wx[0]= x = x0
    wy[0]= y = y0
    for i in range(1,n+1):
        f1 = f(x,y)
        f2 = f(x + h, y + h*f1)
        wx[i] = x = x0 + i * h
        wy[i] = y = y + (h*(f1+f2))/2.0
    return wx, wy

def f(x, y):
    return 3*y+0.5*x
 
wx, wy = ModEul(f, 0, 1, 1, 5)
for x, y in list(zip(wx, wy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, ((19/18)*math.exp(3*x)\
    -(1/6)*x-(1/18)), abs(y-((19/18)*math.exp(3*x)-(1/6)*x-(1/18)))))                                                  
    plt.plot(wx, wy,'r-',lw=1, label='Modified-Euler')
    plt.plot(vx, vy,'b-', lw=1, label='Runge-Kutta')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.show()

#=====================================
def ModEul(f,x0,y0,x1,n):
    wx = [0]*(n+1)
    wy = [0]*(n+1)
    h = (x1-x0)/float(n)
    wx[0]= x = x0
    wy[0]= y = y0
    for i in range(1,n+1):
        f1 = f(x,y)
        f2 = f(x + h, y + h*f1)
        wx[i] = x = x0 + i * h
        wy[i] = y = y + (h*(f1+f2))/2.0
    return wx, wy
    
def f(x, y):
    return (2*math.cos(x**2)-math.sin(x**2)+y**2)/2*math.cos(x)
 
wx, wy = ModEul(f, 0, -1, 1, 20)
for x, y in list(zip(wx, wy))[::2]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x))), abs(y - (math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x)))))))
    plt.plot(wx, wy,'ro',lw=1, label='Modified-Euler')
    plt.plot(vx, vy,'b-', lw=1, label='Runge-Kutta')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.show()
