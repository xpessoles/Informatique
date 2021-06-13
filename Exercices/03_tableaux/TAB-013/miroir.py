def miroir(t):
    """Renverse t"""
    n = len(t)
    return [t[n-1-i] for i in range(n)]
