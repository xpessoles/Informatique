#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


from tkinter import *
from math import sin, cos, radians

# ------------------------ commandes logo --------------------------
def fpos(x0,y0):
    # place la tortue en (x0; y0)
    global x,y
    x = x0
    y = y0
    
def fcap(angle0):
    global angle
    # oriente la tortue dans une direction (en degrés)angle = angle0
    angle = angle0
    
def av(d):
    # avance en dessinant
    global x, y
    x2 = x + d*cos(angle)
    y2 = y + d*sin(angle)
    can.create_line(x, y, x2, y2, width=2, fill="black")
    x = x2
    y = y2
    
def tg(a):
    # tourne à gauche de a degrés
    global angle
    angle -= radians(a)
# -------------------------------------------------------------------
def dragon(t,vz):
    if t==0:
        av(15)
    else:
        dragon(t-1,1)
        tg(vz*90)
        dragon(t-1,-1)

def dessiner():
    fpos(300,600)
    fcap(0)
    dragon(0,1)
    
fen = Tk()
can = Canvas(fen, bg='white', height=800, width=800)
can.pack(side=TOP)
# Boutons
bou1 = Button(fen, text='Quitter', width=10, command=fen.quit)
bou1.pack(side=RIGHT)
dessiner()
fen.mainloop()
fen.destroy()
