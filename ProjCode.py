# -*- coding: utf-8 -*-
"""
Created on Tue March  13 22:48:43 2018

@author: Adeseto, AKINWE
"""
import math
from matplotlib import pyplot as plt

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
 
def exact(x):    
    return ((19/18)*math.exp(3*x)-(1/6)*x-(1/18))

def error(x,y):    
    return abs(y-exact(x))
wx, wy = rk4(f, 0, 1, 1, 5)
for x, y in list(zip(wx, wy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, exact(x), error(x,y)))
    plt.plot(wx, wy,'r-',lw=1, label='Modified-Euler')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
#=========================================================
import math
from matplotlib import pyplot as plt

def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy
 
def f(x, y):
    return 3*y+0.5*x
def exact(x):    
    return ((19/18)*math.exp(3*x)-(1/6)*x-(1/18))

def error(x,y):    
    return abs(y-exact(x))
vx, vy = rk4(f, 0, 1, 1, 5)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, exact(x), error(x,y)))
    plt.plot(vx, vy, 'b-', lw=1, label= 'Exact')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Exact values (y)')
    plt.title(r'$h=0.05$')
    plt.legend(loc='best')
    plt.grid(True)
