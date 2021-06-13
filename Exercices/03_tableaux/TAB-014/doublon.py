def doublon(t):
    """Renvoie un booléen indiquant s'il y a un doublon dans t"""
    n = len(t)
    for i in range(n-1):
        # Invariant : les éléments de t[:i] n'ont pas de doublon
        for j in range(i+1,n):
            # Invariant : t[i] ne se trouve pas dans t[i+1:j]
            if t[i] == t[j]:
                return True
    return False

def doublon_rapide(t):
    return len(set(t)) != len(t)
