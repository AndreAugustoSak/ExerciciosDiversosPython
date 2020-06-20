def carta_faltante(a, b, c):
    if a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a
    return d




print(carta_faltante(55, 22, 22))
