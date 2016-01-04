import random



def tri_bulles_naif(l):
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]


def tri_bulles(l):
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

"""
l = [random.randint(0,10) for i in range(10)]
print(l)
tri_bulles_naif(l)
print(l)
"""

l = [random.randint(0,10) for i in range(10)]
print(l)
tri_bulles(l)
print(l)

