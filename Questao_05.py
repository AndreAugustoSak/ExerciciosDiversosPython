def nome_curto(nome):
    nome_lista = nome.split(' ')
    return nome_lista[0] + ' ' + nome_lista[-1]


print(nome_curto('Terence David John Pratchett'))
