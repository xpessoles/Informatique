# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:49:24 2022

@author: xpess
"""

from collections import deque

pile = deque()
for i in range(10):
    pile.append(i)


def copy_pile(pile):
    pile_tmp = deque()
    pile_copy = deque()
    
    while pile : 
        pile_tmp.append(pile.pop())
        
    while pile_tmp : 
        el= pile_tmp.pop()
        pile.append(el)
        pile_copy.append(el)
    return pile_copy
    
    
def hauteur(pile) -> int : 
    pile_tmp = deque()
    h = 0
    while pile : 
        pile_tmp.append(pile.pop())
        h = h+1
    while pile_tmp : 
        pile.append(pile_tmp.pop())
    return h


def hauteur_rec(pile):
    # /!\ on perd la pile

    if not pile : 
        return 0
    else :
        pile.pop()
        return 1+hauteur_rec(pile)
    
def reverse(pile):
    pile_tmp = deque()
    pile_tmp2 = deque()

    while pile : 
        pile_tmp.append(pile.pop())
    while pile_tmp : 
        pile_tmp2.append(pile_tmp.pop())
    while pile_tmp2 : 
        pile.append(pile_tmp2.pop())
    
    
file = deque()
for i in range(10):
    file.append(i)
    
def copy_file(file):
    file_tmp = deque()
    file_copy = deque()
    while file : 
        print(file_tmp)
        file_tmp.append(file.popleft())
        
    while file_tmp : 
        el= file_tmp.popleft()
        file.append(el)
        file_copy.append(el)
    return file_copy
    
    
def longueur(file) -> int : 
    file_tmp = deque()
    l = 0
    while file : 
        file_tmp.append(file.popleft())
        l = l+1
    while file_tmp : 
        file.append(file_tmp.popleft())
    return l