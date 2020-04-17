# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 04:12:24 2019

@author: RICHKINWE
"""
#using the tkinter library for GUI
from tkinter import *
window=Tk()
window.title('Kg Converter')
def kg_gpo():
    gram=float(e_val.get())*1000
    pound=float(e_val.get())*2.20462
    ounce=float(e_val.get())*35.274
    t1.delete('1.0',END)
    t1.insert(END,gram)
    t2.delete('1.0',END)
    t2.insert(END,pound)
    t3.delete('1.0',END)
    t3.insert(END,ounce)

l=Label(window,text='kg')
l.grid(row=0,column=0)

e_val=IntVar()
e=Entry(window,textvariable=e_val)
e.grid(row=0, column=1)

b=Button(window,text='convert',command=kg_gpo)
b.grid(row=0, column=2)

t1=Text(window,height=1, width=20)
t1.grid(row=1,column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()