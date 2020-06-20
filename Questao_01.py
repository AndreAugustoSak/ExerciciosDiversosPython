def dias_premio(lista):
    qtd_dias = 0
    for c in lista:
        c += c
        qtd_dias += 1
        if c >= 1000000:
            return qtd_dias


print(dias_premio([100000, 250000, 250000, 500000]))
