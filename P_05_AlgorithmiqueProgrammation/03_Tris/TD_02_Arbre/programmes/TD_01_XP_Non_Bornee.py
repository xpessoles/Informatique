#!/usr/bin/env python
# -*- coding: utf-8 -*-


def creer_pile(n):
    return []

def est_vide(pile):
    return len(pile)==0

def empiler(pile,el) :
    return pile.append(el)
    
def depiler(pile):
    return pile.pop()

def long_pile(pile):
    return len(pile)
    
# Exercice 1 : Parenthèses
# ========================
# D'après IPT en CPGE Wack & All

def parentheses(s):
    pile = creer_pile(len(s))
    for i in range(len(s)):
        if s[i] == "(":
            empiler(pile,i)
        else :
            if est_vide(pile):
                return False
            j=depiler(pile)
            # print(j,i) # Pour la question 1
    return est_vide(pile) # Pour la question 2

def parentheses_2(s):
    pile = creer_pile(len(s))
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            empiler(pile,i)
        else :
            if est_vide(pile):
                return False
            j=depiler(pile)
            if j=="(" and s[i]!=")" :
                return False
            if j=="[" and s[i]!="]" :
                return False
            if j=="{" and s[i]!="}" :
                return False
    return est_vide(pile) 


def parentheses_3(s):
    pile = creer_pile(len(s))
    for i in range(len(s)):
        if s[i] in ["(",")","{","}","[","]"]:
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                empiler(pile,i)
            else :
                if est_vide(pile):
                    return False
                j=depiler(pile)
                if j=="(" and s[i]!=")" :
                    return False
                if j=="[" and s[i]!="]" :
                    return False
                if j=="{" and s[i]!="}" :
                    return False
    return est_vide(pile) 
s = "(()()())"
s2 = "((){[]}())"
s3 = "(a(a)a{a[a]a}a(a)a)"

#print(parentheses_3(s3))

# Exercice 2 : Inversion
# ======================
def inversion(pile):
    el1 = depiler(pile)
    el2 = depiler(pile)
    empiler(pile,el1)
    empiler(pile,el2)

# Exercice 3 : Dépiler le nième (en partant du bas de la pile - Comptage à partir de 1)
# =============================
def depile_n(pile,n):
    taille = long_pile(pile)
    taille2 = taille-n
    pile2 = creer_pile(taille2)
    j=0
    while j<=taille2:
        empiler(pile2,depiler(pile))
        j = j+1
    el = depiler(pile2)
    while est_vide(pile2) == False:
        empiler(pile,depiler(pile2))
    return el

pile=[0,1,2,3,4,5,6,7,8]
print(pile)
print(depile_n(pile,3))
print(pile)