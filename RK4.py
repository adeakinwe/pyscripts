# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:47:54 2018

@author: RICHKINWE
"""

#RK-4
#using lambda
def RK4(f):
    return lambda t, y, dt: (
            lambda dy1: (
            lambda dy2: (
            lambda dy3: (
            lambda dy4: (dy1 + 2*dy2 + 2*dy3 + dy4)/6
            )( dt * f( t + dt  , y + dy3   ) )
	    )( dt * f( t + dt/2, y + dy2/2 ) )
	    )( dt * f( t + dt/2, y + dy1/2 ) )
	    )( dt * f( t       , y         ) )
 
def theory(t): return (t**2 + 4)**2 /16
 
from math import sqrt
dy = RK4(lambda t, y: t*sqrt(y))
 
t, y, dt = 0., 1., .1
while t <= 10:
    if abs(round(t) - t) < 1e-5:
        print("y(%2.1f)\t= %4.6f \t error: %4.6g" % ( t, y, abs(y - theory(t))))
    t, y = t + dt, y + dy( t, y, dt )
 
 
Output:
y(0.0)	= 1.000000 	 error:    0
y(1.0)	= 1.562500 	 error: 1.45722e-07
y(2.0)	= 3.999999 	 error: 9.19479e-07
y(3.0)	= 10.562497 	 error: 2.90956e-06
y(4.0)	= 24.999994 	 error: 6.23491e-06
y(5.0)	= 52.562489 	 error: 1.08197e-05
y(6.0)	= 99.999983 	 error: 1.65946e-05
y(7.0)	= 175.562476 	 error: 2.35177e-05
y(8.0)	= 288.999968 	 error: 3.15652e-05
y(9.0)	= 451.562459 	 error: 4.07232e-05
y(10.0)	= 675.999949 	 error: 5.09833e-05

#Alternate solution
#from math import sqrt
 
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
def exact(x):
    return (3*math.exp(x**2/2)-x**2-2)

def error(x,y):
    return abs(y-exact(x))
 
vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("y(%4.2f) %10.5f    error:%+12.4e" % (x, y, error(x,y)))
    
 0.0    1.00000  +0.0000e+00
 1.0    1.56250  -1.4572e-07
 2.0    4.00000  -9.1948e-07
 3.0   10.56250  -2.9096e-06
 4.0   24.99999  -6.2349e-06
 5.0   52.56249  -1.0820e-05
 6.0   99.99998  -1.6595e-05
 7.0  175.56248  -2.3518e-05
 8.0  288.99997  -3.1565e-05
 9.0  451.56246  -4.0723e-05
10.0  675.99995  -5.0983e-05

#TEST_CASES
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
    return x+y
 
vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("y(%4.2f) %10.5f  %10.5f  error:%+12.4e" % (x,y, abs(y-2*math.exp(x)-x-y)))
print("y(%4.2f) %10.5f  %10.5f  error:%+12.4e" % (x,y, abs(y-2*math.exp(x)-x-y))) 
    #using lambda
def RK4(f):
    return lambda t, y, dt: (
            lambda dy1: (
            lambda dy2: (
            lambda dy3: (
            lambda dy4: (dy1 + 2*dy2 + 2*dy3 + dy4)/6
            )( dt * f( t + dt  , y + dy3   ) )
	    )( dt * f( t + dt/2, y + dy2/2 ) )
	    )( dt * f( t + dt/2, y + dy1/2 ) )
	    )( dt * f( t       , y         ) )
 
def theory(t): return  2+(1/(-0.33-0.67(exp(-3*t))))
 
from math import sqrt
dy = RK4(lambda t, y: y**2-y-2
 
t, y, dt = 0., 1., .1
while t <= 10:
    if abs(round(t) - t) < 1e-5:
        print("y(%2.1f)\t= %4.6f \t error: %4.6g" % ( t, y, abs(y - theory(t))))
    t, y = t + dt, y + dy( t, y, dt )
----------------------------------------------------------
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
    return x+y


vx, vy = rk4(f, 0, 1, 1, 10)
for x, y in list(zip(vx, vy))[:]:
    print("%4.1f %10.16f %10.16f   error:%12.4e" % (x,y, 2*math.exp(x)-x-1, abs(y-2*math.exp(x)-x-1)))