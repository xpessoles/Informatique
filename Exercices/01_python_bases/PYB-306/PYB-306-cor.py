def appartient(a,c,r):
    """Dit si a est dans le cercle de centre c, de rayon r"""
    xa,ya = a
    xc,yc = c
    return (xa-xc)**2 + (ya-yc)**2 <= r**2
