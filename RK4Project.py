# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:39:27 2018

@author: Adeseto, AKINWE
"""
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
    return x**3+x*y
 
vx, vy = rk4(f, 0, 1, 1, 5)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))
    plt.plot(vx, vy,'r-', linewidth=1, label='approximation')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title('h=0.05')
    #plt.legend(loc='best')
    plt.grid(True)
    #plt.show()
#--------------------------------------------------------------------------------------------

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
    return y**2-y-2
 
vx, vy = rk4(f, 0, 1, 1, 5)
for x, y in list(zip(vx, vy))[:]:
    print("%1.2f %10.16f %10.16f   %12.4e" % (x, y,(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))), abs(y-(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))))))
    plt.plot(vx, vy,'r-',label='approximation')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.1')
   # plt.legend(loc='best')
    plt.grid()
   
#-----------------------------------------------------------------------------------------------------
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
    return (2*math.cos(x**2)-math.sin(x**2)+y**2)/2*math.cos(x)
 
vx, vy = rk4(f, 0, -1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x))), abs(y-(math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x)))))))
    plt.plot(vx, vy,'r-',label='approximation')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.2')
   # plt.legend(loc='best')
    plt.grid()
   
#==================================================================
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
    #plt.show()
#======================================================================
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
    return x*y-y**2
 
vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 2*math.exp(x**2/2)/(math.sqrt(2*math.pi)*math.erf(x/math.sqrt(2))+2), abs(y-(2*math.exp(x**2/2)/(math.sqrt(2*math.pi)*math.erf(x/math.sqrt(2))+2)))))
#==========================================
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
    return x**2+x*y
 
vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, math.sqrt(math.pi/2)*math.exp(0.5*x**2)*math.erf(x/math.sqrt(2)) + math.exp(0.5*x**2)-x, abs(y-(math.sqrt(math.pi/2)*math.exp(0.5*x**2)*math.erf(x/math.sqrt(2))+math.exp(0.5*x**2)-x))))
