
import math

def fonction_1(x):
    return x*math.log(x)-1

def fonction_d1(x):
    return math.log(x)+1

def dichotomie (f,epsilon):
    a = 1
    b = math.e
    cpt=0
    while abs(a-b)>epsilon : 
        cpt = cpt+1
        c=(a+b)/2
        print(a-b,f(c))
        if f(a)*f(c)<0 :
            b=c
        else :
            a=c
    print("Dichotomie "+str(cpt))
    return (a+b)/2


    
def lagrange(f,epsilon):
    a = 1
    b = math.e
    c=(a+b)/2
    cpt=0
    while abs(a-b)>epsilon and cpt<100: 
        c = (b*f(a)-a*f(b))/(f(a)-f(b))
        cpt = cpt+1
        if f(a)*f(c)<0 :
            b=c
        else :
            a=c
    print("Lagrange "+str(cpt))
    return (a+b)/2


def newton(f,fp,epsilon):
    x = 2.8
    cpt=0
    while abs(x-1.763223)>epsilon:
        x = x-f(x)/fp(x)
        cpt = cpt+1
    print("Newton "+str(cpt))
    return x

#res = dichotomie(fonction_1,0.000001)
#print(res, fonction_1(res))

#res = lagrange(fonction_1,0.000001)
#print(res, fonction_1(res))

#res = newton(fonction_1,fonction_d1,0.000001)
#print(res, fonction_1(res))

def f2(x,n):
    return x**n+x**(n-1)+x-1

def dichotomie2 (f,n,epsilon):
    a = 0
    b = 1
    cpt=0
    while abs(a-b)>epsilon : 
        cpt = cpt+1
        c=(a+b)/2
        
        if f(a,n)*f(c,n)<0 :
            b=c
        else :
            a=c
    #print("Dichotomie "+str(cpt))
    return (a+b)/2

for i in range(999,1000):
    #print(i)
    res = dichotomie2(f2,i,0.0001)
    print(res, f2(res,i))

