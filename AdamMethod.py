# -*- coding: utf-8 -*-
"""
Created on Mon May 28 22:46:32 2018

@author: RICHKINWE
"""

import numpy as np
import matplotlib.pyplot as plt


def feval(funcName, *args):
    return eval(funcName)(*args)


def RungeKutta4thOrder(func, yinit, xspan, h):
    m = len(yinit)
    n = int((xspan[-1] - xspan[0]) / h)

    x = xspan[0]
    y = yinit

    xsol = np.empty((0))
    xsol = np.append(xsol, x)

    ysol = np.empty((0))
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)

        yp2 = y + k1*(h/2)

        k2 = feval(func, x+h/2, yp2)

        yp3 = y + k2*(h/2)

        k3 = feval(func, x+h/2, yp3)

        yp4 = y + k3*h

        k4 = feval(func, x+h, yp4)

        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])

        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  # Save all new y's

    return [xsol, ysol]


def ABM4thOrder(func, yinit, xspan, h):

    m = len(yinit)

    dx = int((xspan[-1] - xspan[0]) / h)

    xrk = [xspan[0] + k * h for k in range(dx + 1)]

    [xx, yy] = RungeKutta4thOrder(func, yinit, (xrk[0], xrk[3]), h)

    x = xx
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    y = yy
    yn = np.array([yy[0]])
    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(3, dx):
        x00 = x[i]; x11 = x[i-1]; x22 = x[i-2]; x33 = x[i-3]; xpp = x[i]+h

        y00 = np.array([y[i]])
        y11 = np.array([y[i - 1]])
        y22 = np.array([y[i - 2]])
        y33 = np.array([y[i - 3]])

        y0prime = feval(func, x00, y00)
        y1prime = feval(func, x11, y11)
        y2prime = feval(func, x22, y22)
        y3prime = feval(func, x33, y33)

        ypredictor = y00 + (h/24)*(55*y0prime - 59*y1prime + 37*y2prime - 9*y3prime)
        ypp = feval(func, xpp, ypredictor)

        for j in range(m):
            yn[j] = y00[j] + (h/24)*(9*ypp[j] + 19*y0prime[j] - 5*y1prime[j] + y2prime[j])

        xs = x[i] + h
        xsol = np.append(xsol, xs)

        x = xsol

        for r in range(len(yn)):
            ysol = np.append(ysol, yn)

        y = ysol

    return [xsol, ysol]


def myFunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = (1/2)*(x - y[0])
    return dy


h = 0.2
xspan = np.array([0.0, 3.0])
yinit = np.array([1.0])


[ts, ys] = ABM4thOrder('myFunc', yinit, xspan, h)


dt = int((xspan[-1]-xspan[0])/h)
t = [xspan[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = t[i] - 2 + 3*np.exp(-0.5*t[i])
    yexact.append(ye)

diff = ys - yexact
for p,q, w, z in list(zip(ts, ys, yexact, diff))[:]:
    print("%4.1f  %10.16f  %10.16f %12.4e" % (p, q, w, abs(z)))
print("Maximum difference =", np.max(abs(diff)))
#wx, wy = ModEul(f, 0, 1, 1, 5)
#for x, y in list(zip(wx, wy))[:]:
#    print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))

plt.plot(ts, ys, 'ro')
plt.plot(t, yexact, 'b')
plt.xlim(xspan[0], xspan[1])
plt.legend(["ABM 4th Order ", "Exact solution"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.grid(True)
plt.tight_layout()
plt.show()