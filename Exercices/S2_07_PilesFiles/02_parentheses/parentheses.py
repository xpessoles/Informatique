# -*- coding: utf-8 -*-

## importation des modules
from collections import deque
import pdb
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



def verifPar12(texte):
    p = deque()
    for c in texte:
        #print(p)
        if c in '([{':
            p.append(c)
        elif c in ')]}':
            #pdb.set_trace()
            if len(p)==0:
                return -1
            else:
                x=p.pop()
                if c==')' and x!='(':
                    return c
                elif c=='{' and x!='}':
                    return c
                elif c=='[' and x!=']':
                    return c
    return len(p)



## programme principal

print(verifPar0('(()())'))  # 0
print(verifPar0('(()()'))   # 1
print(verifPar0('(()()))')) # -1

print('{[()} : ',verifPar1('{[()}'),verifPar12('{[()}'))   # }
print('{[()] : ',verifPar1('{[()]'),verifPar12('{[()]'))   # 1
print('{[()]} : ',verifPar1('{[()]}'),verifPar12('{[()]}'))  # 0

