def mediane(t):
    """Calcule une médiane de t"""
    tab = t.copy()
    while len(tab) > 2:
        M = max(tab)
        m = min(tab)
        tab.remove(m)
        tab.remove(M)
    return (tab[0]+tab[-1])/2
