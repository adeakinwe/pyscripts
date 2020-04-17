# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:52:51 2018

@author: RICHKINWE
"""
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
        y[i] = y[i-1]+ h*(f1+f2)/2.0
    return x, y

def f(x, y):
    return x**3+x*y
 
x, y = ModEul(f, 0, 1, 5,(0,1))
for x, y in list(zip(x, y))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))
    plt.plot(x, y,'ro',lw=1, label='ModEuler')
    plt.plot(vx, vy,'b-', lw=1, label='approximation')
    plt.xlabel(r'Mesh values$(x_n)$')
    plt.ylabel(r'Approximation $y(x_n)$')
    plt.title('h=0.2')
    #plt.legend(loc='best')
    plt.grid(True)
    #plt.show()
#=======================================================
import math
from matplotlib import pyplot 
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
        y[i] = y[i-1]+ h*(f1+f2)/2.0
    return x,y
      
def f(x, y):
    return y**2-y-2
 
x, y = ModEul(f, 0, 1, 10, (0,1))
for x, y in list(zip(x, y))[:]:
    print("%1.2f   %10.16f   %10.16f   %12.4e" % (x, y,(-1+(1/((1/3)+(1/6)*math.exp(3*x)))), abs(y-(-1+(1/((1/3)+(1/6)*math.exp(3*x)))))))
#===========================================================
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
        y[i] = y[i-1]+ h*(f1+f2)/2.0
    return x, y

def f(x, y):
    return 3*y+0.5*x
 
x, y = ModEul(f, 0, 1, 5,(0,1))
for x, y in list(zip(x, y))[:]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, ((19/18)*math.exp(3*x)-(1/6)*x-(1/18)), abs(y-((19/18)*math.exp(3*x)-(1/6)*x-(1/18)))))
    plt.plot(x, y,'ro', label='ModEuler')
    plt.plot(vx, vy, 'b-', label='Runge-Kutta')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.2')
    #plt.legend(loc='best')
    plt.grid(True)
    #+++++++++++++++++++++++++++++++++++++
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
        y[i] = y[i-1]+ h*(f1+f2)/2.0
    return x, y

def f(x, y):
    return (2*math.cos(x**2)-math.sin(x**2)+y**2)/2*math.cos(x)
 
x, y = ModEul(f, 0, 1, 20,(0,-1))
for x, y in list(zip(x, y))[::2]:
    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x))), abs(y - (math.sin(x)+(1/(-0.5*math.sin(x)-math.cos(x)))))))
#================================================
    p=math.sqrt(math.pi/2)*math.exp(0.5*x**2)*math.erf(x/math.sqrt(2))+math.exp(0.5*x**2)-x
    q=2*math.exp(x**2/2)/(math.sqrt(2*math.pi)*math.erf(x/math.sqrt(2))+2)