# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 09:18:12 2014

@author: ericguichet
"""

import numpy as np
import matplotlib.pyplot as plt

def afficher(A):
    plt.xticks([])
    plt.yticks([])
    plt.imshow(A,cmap=plt.cm.gray)

def f(x):
    return (0.5+0.5*np.sin((x/255-0.5)*np.pi))*255

def augmenter_contraste(A,k):
    B=A
    for i in range(k):
        B=f(B)
    return B

chat=np.fromfile("chat_260_335.txt",float,-1," ").reshape(260,335)

plt.subplot(121)
afficher(chat)
plt.subplot(122)
afficher(augmenter_contraste(chat,2))

plt.show()