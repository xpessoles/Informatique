# -*- coding: utf-8 -*-
"""
@auteur: David Fournier
"""

s = [3,4,8,11,1,5,2,7,9,0,10,0]

def scm(s):
    r = []
    d, f = 0, 0
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            f += 1
        else:
            r.append((d,f))
            d = f = f+1
    r.append((d,f))
    return r

r = scm(s)
#print(r)

def fusionnerRec(s, r1, r2):
    # Ne réponds à la question car pas en place.
    d1, f1 = r1
    d2, f2 = r2
    if d1 > f1 or d2 > f2:
        return s
    else:
        assert f1+1 == d2
        if s[d1] <= s[d2]:
            return fusionnerRec(s, (d1+1, f1), r2)
        else:
            s0 = s[:d1]
            s1 = s[d1:f1+1]
            s2 = s[d2:f2+1]
            s4 = s[f2+1:]
            f1 = d1 + len(s2) - 1
            d2 = f1 + 1
            return fusionnerRec(s0+s2+s1+s4, (d1,f1), (d2,f2))
          
#print(s)
#fusionnerRec(s, r[0], r[1])
#print(s)

def fusionnerEnPlaceRec(s, r1, r2):
    d1, f1 = r1
    d2, f2 = r2
    if d1 > f1 or d2 > f2:
        return s
    else:
        assert f1+1 == d2
        if s[d1] <= s[d2]:
            return fusionnerEnPlaceRec(s, (d1+1, f1), r2)
        else:
            for i in range(f2-d2+1):
                t = s.pop(f2) # Interdit par le sujet
                s.insert(d1,t) # Interdit par le sujet
            f1 = d1 + (f2-d2+1) - 1
            d2 = f1 + 1
            return fusionnerEnPlaceRec(s, (d1,f1), (d2,f2))

#print(s)
#fusionnerEnPlaceRec(s, r[0], r[1])
#print(s)

def fusionnerWhile(s, r1, r2):
    d1, f1 = r1
    d2, f2 = r2
    while d1<f2:
        if s[d1] <= s[d2]:
            d1 += 1
        else:
            s0 = s[:d1]
            s1 = s[d1:f1+1]
            s2 = s[d2:f2+1]
            s3 = s[f2+1:]
            f1 = d1 + len(s2) - 1
            d2 = f1 + 1
            s[:] = s0+s2+s1+s3 # Permutation de s2 et s1 pour que le test soit vrai à la prochaine itération

#print(s)
#fusionnerWhile(s, r[0], r[1])
#print(s)

def fusionner(s, r1, r2):
    d1, f1 = r1
    d2, f2 = r2
    s1, i1 = s[d1:f1+1], 0
    s2, i2 = s[d2:f2+1], 0
    for i in range(d1,f2+1):
        if i1 > len(s1)-1:
            s[i] = s2[i2]
            i2 += 1
        elif i2 > len(s2)-1:
            s[i] = s1[i1]
            i1 += 1
        elif s1[i1] <= s2[i2]:
            s[i] = s1[i1]
            i1 += 1
        else:
            s[i] = s2[i2]
            i2 += 1

#print(s)
#fusionner(s, r[0], r[1])
#print(s)

