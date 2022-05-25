# -*- coding: utf-8 -*-

## importation des modules
from collections import deque

## déclaration des fonctions
def verifPar0(texte):
    p = deque()
    for c in texte:
        if c == '(':
            p.append(c)
        elif c == ')':
            if len(p) > 0:
                p.pop()
            else:
                return -1
    return len(p)

def verifPar1(texte):
    p = deque()
    for c in texte:
        if c in '([{':
            p.append(c)
        elif c in ')]}':
            if len(p) > 0:
                ouverture = p.pop()
                if ouverture == '(' and c != ')':
                    return c
                elif ouverture == '[' and c != ']':
                    return c
                elif ouverture == '{' and c != '}':
                    return c
            else:
                return -1
    return len(p)

def

## programme principal

print(verifPar0('(()())'))  # 0
print(verifPar0('(()()'))   # 1
print(verifPar0('(()()))')) # -1

print(verifPar1('{[()}'))   # }
print(verifPar1('{[()]'))   # 1
print(verifPar1('{[()]}'))  # 0

