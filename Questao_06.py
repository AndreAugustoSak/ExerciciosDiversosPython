def verifica_hora(hora):
    lista = hora.split(':')
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    if lista[0] > 23:
        return False
    elif lista[1] > 59:
        return False
    elif lista[2] > 59:
        return False
    else:
        return True


print(verifica_hora('15:30:00'))
