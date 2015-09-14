#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi

def TracerSegment(L,ori,x,y):
    #print("appel",x,y)
    x.append(x[-1]+L*cos(ori*pi/2))
    y.append(x[-1]+L*sin(ori*pi/2))
    print("appel",x,y)
    return x,y

def DessineDragon(n,ori):
    x,y=[0],[0]
    L=1
    if n==0 :
        print("appel",x,y)
        x,y = TracerSegment(L,ori,x,y)
        print("",x,y)
    else :
        DessineDragon(n-1,ori)
        ori = -ori
        DessineDragon(n-1,ori)
    return x,y
    
x,y = DessineDragon(2,1)
    
print(x,y)