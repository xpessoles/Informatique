alpha = 16

def u(alpha,n):
    """u_n, u_0 = alpha"""
    x = alpha
    for i in range(n):
        x = (15091 * x) % 64007
    return x


def pyramide(alpha,n):
    p = []
    x = alpha
    for i in range(n):
        l = []
        for j in range(i+1) :
            y = x % 10
            l.append(y)
            x = (15091 * x) % 64007
        p.append(l)
    return p

t20 = pyramide(alpha,20)

def total (p) :
    n = len(p)
    m = 0
    for ligne in range(n) :
        for j in range(n-ligne-1) :
            p[n-ligne-2][j] += max(p[n-ligne-1][j],p[n-ligne-1][j+1])
    return p[0][0]
        
