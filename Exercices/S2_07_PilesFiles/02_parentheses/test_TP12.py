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



## Tests

print(verifPar0('(()())'))  # 0
print(verifPar0('(()()'))   # 1
print(verifPar0('(()()))')) # -1

print(verifPar1('{[()}'))   # }
print(verifPar1('{[()]'))   # 1
print(verifPar1('{[()]}'))  # 0


from math import sqrt, exp, log
op_uni = {'sqrt': sqrt, 'exp': exp, 'ln':log}
def add(x, y):
    return x + y
def sous(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
op_bin = {'+': add, '-': sous, '*': mult, '/': div}


evalue([3,2,'+',7,'*','sqrt'])

def evalue(lst):
    p = deque()
    for t in lst:
        if t in op_bin:
            y = p.pop()
            x = p.pop()
            p.append(op_bin[t](x, y))
        elif t in op_uni:
            x = p.pop()
            p.append(op_uni[t](x))
        else:
            p.append(t)
    return p.pop()


def evalue2(lst):
    p = deque()
    for t in lst:
        if t in op_bin:
            if p.empty():
                raise ValueError("expression incorrecte")
            y = p.pop()
            if p.empty():
                raise ValueError("expression incorrecte")
            x = p.pop()
            p.push(op_bin[t](x, y))
        elif t in op_uni:
            if p.empty():
                raise ValueError("expression incorrecte")
            x = p.pop()
            p.push(op_uni[t](x))
        else:
            p.push(t)
    s = p.pop()
    if not p.empty():
        raise ValueError("expression incorrecte")
    return s