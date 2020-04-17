# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:22:00 2018

@author: RICHKINWE
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return y**2-y-2
 
vx, vy = rk4(f, 0, 1, 0.4, 10)
for x, y in list(zip(vx, vy))[:]:
    #print("%1.2f %10.16f %10.16f   %12.4e" % (x, y,(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))), abs(y-(2+(1/(-(1/3)-(2/3)*math.exp(-3*x)))))))
    p, q = ModEl(f, 0, 0.4, 10, (0,1))
for p, q in list(zip(p, q))[:]:
   #print("%1.2f %10.16f %10.16f   %12.4e" % (p, q,(2+(1/(-(1/3)-(2/3)*math.exp(-3*p)))), abs(q-(2+(1/(-(1/3)-(2/3)*math.exp(-3*p)))))))
    plt.plot(vx, vy,'b-', label=('approximation'))
    plt.plot(x,y,'r-')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.1')
   # plt.legend()
    plt.grid()
    #plt.show()
#==================================
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return y**2-y-2
 
    p, q = ModEl(f, 0, 0.4, 10, (0,1))
for p, q in list(zip(p, q))[:]:
    vx, vy = rk4(f, 0, 1, 0.4, 10)
for x, y in list(zip(vx, vy))[:]:
    print("%1.2f %10.16f %12.4e %10.16f %12.4e  %10.16f" % (x,q,abs(q-(2+(1/(-(1/3)-(2/3)*math.exp(-3*x))))),  y, abs(y-(2+(1/(-(1/3)-(2/3)*math.exp(-3*x))))),(2+(1/(-(1/3)-(2/3)*math.exp(-3*x))))))
   #print("%1.2f %10.16f %10.16f   %12.4e" % (p, q,(2+(1/(-(1/3)-(2/3)*math.exp(-3*p)))), abs(q-(2+(1/(-(1/3)-(2/3)*math.exp(-3*p)))))))
#================================
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
 
vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    #for x, y in list(zip(vx, vy))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))
 
   #===========
   
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
#===========================
import math
from matplotlib import pyplot as plt
import numpy as np
#a=0;b=2, N=10,
def ModEul(f,a,b,N,IV):
    h = (b-a)/float(N)
    x = np.arange(a,b+h,h)
    y = np.zeros((N+1,))
    x[0],y[0]= IV
    for i in range(1,N+1):
        f1 = f(x[i-1],y[i-1])
        f2 = f(x[i], y[i-1] + h*f1)
        y[i] = y[i-1]+ h*(f1+f2)/2
    return x, wy

def f(x, y):
    return x+y
 
x, y = ModEul(f, 0, 1, 10,(0,1))
for x, y in list(zip(x, y))[:]:
    print("%4.1f  %10.16f " % (x, y))
    plt.plot(vx, vy,'bo', x, y, 'ro')
   # plt.plot(x,y,'ro')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.1')
   #plt.legend(loc='best')
    plt.grid(True)
   