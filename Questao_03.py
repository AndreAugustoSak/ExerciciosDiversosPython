def calcula_juros_compostos(c, j, t):
    j = float((j).rstrip('%'))
    j = j/100
    m = c * ((1+j)**t)
    return m - c


print(calcula_juros_compostos(830.50,'1%',12))

