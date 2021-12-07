
def moyenne (a,b):
    """Moyenne de a et b"""
    return (int(a) + int(b)/2)

def listing(a):
    if isinstance(a, int):
        for i in range(a+1):
            texte = print("-",i)
    else:
        for i in a:
            texte = print("-",i)
    return texte