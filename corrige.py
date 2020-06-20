import provaP2 as P2

def teste_dias_premio():
    try:
        valor = 1.0
        testes = 0
        if P2.dias_premio ([100,99900,400000,500000,600000]) == 4: testes += 1
        if P2.dias_premio ([1,1000000])                      == 2: testes += 1
        if P2.dias_premio ([100000,250000,250000 ,500000])   == 4: testes += 1
        if testes < 3:
            print('Funcao dias_premio NÃO está OK')
        else:
            print('Funcao dias_premio está OK')
        return(valor * (testes/3))
    except AttributeError:
        print ('Funcao dias_premio não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao dias_premio deu erro na execução')
        return(valor * (testes/3))

def teste_em_equilibrio():
    try:
        valor = 1.0
        testes = 0
        if P2.em_equilibrio(12,3,3,6)         == True  : testes += 1
        if P2.em_equilibrio(2002,560,560,882) == False : testes += 1
        if P2.em_equilibrio(500,125,125,250)  == True  : testes += 1
        if testes < 3:
            print('Funcao em_equilibrio NÃO está OK')
        else:
            print('Funcao em_equilibrio está OK')
        return(valor * (testes/3))
    except AttributeError:
        print ('Funcao em_equilibrio não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao em_equilibrio deu erro na execução')
        return(valor * (testes/3))

def teste_calcula_juros_compostos():
    try:
        valor = 1.0
        testes = 0
        if abs(102.50 - P2.calcula_juros_compostos(1000,'5%',2)) <= 0.1: testes += 1
        if abs(102.28 - P2.calcula_juros_compostos(2000,'0.5%',10)) <= 0.1: testes += 1
        if abs(105.33 - P2.calcula_juros_compostos(830.50,'1%',12)) <= 0.1: testes += 1
        if testes < 3:
            print('Funcao calcula_juros_compostos NÃO está OK')
        else:
            print('Funcao calcula_juros_compostos está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao calcula_juros_compostos não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao calcula_juros_compostos deu erro na execução')
        return(valor * (testes/3))

def teste_carta_faltante():
    try:
        valor = 1.5
        testes = 0
        if P2.carta_faltante (40,11,40) == 11: testes += 1
        if P2.carta_faltante (8,8,96)   == 96: testes += 1
        if P2.carta_faltante (55,22,22) == 55: testes += 1
        if testes < 3:
            print('Funcao carta_faltante NÃO está OK')
        else:
            print('Funcao carta_faltante está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao carta_faltante não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao carta_faltante deu erro na execução')
        return(valor * (testes/3))

def teste_nome_curto():
    try:
        valor = 1.5
        testes = 0
        if P2.nome_curto('Edgar Allan Poe')              == 'Edgar Poe': testes += 1
        if P2.nome_curto('John Ronald Reuel Tolkien')    == 'John Tolkien': testes += 1
        if P2.nome_curto('Terence David John Pratchett') == 'Terence Pratchett': testes += 1
        if testes < 3:
            print('Funcao nome_curto NÃO está OK')
        else:
            print('Funcao nome_curto está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao nome_curto não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao nome_curto deu erro na execução')
        return(valor * (testes/3))

def teste_verifica_hora():
    try:
        valor = 2.0
        testes = 0
        if P2.verifica_hora('15:30:00') == True: testes += 1
        if P2.verifica_hora('15:00:61') == False: testes += 1
        if P2.verifica_hora('99:99:00') == False: testes += 1
        if testes < 3:
            print('Funcao verifica_hora NÃO está OK')
        else:
            print('Funcao verifica_hora está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao verifica_hora não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao verifica_hora deu erro na execução')
        return(valor * (testes/3))

def teste_ano_bissexto():
    try:
        valor = 2.5
        testes = 0
        if P2.ano_bissexto(2020) == True: testes += 1
        if P2.ano_bissexto(2019) == False: testes += 1
        if P2.ano_bissexto(1600) == True: testes += 1
        if testes < 3:
            print('Funcao ano_bissexto NÃO está OK')
        else:
            print('Funcao ano_bissexto está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao ano_bissexto não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao ano_bissexto deu erro na execução')
        return(valor * (testes/3))

def teste_passa_pela_janela():
    try:
        valor = 3.0
        testes = 0
        if P2.passa_pela_janela(30,50,80,80,60) == True: testes += 1
        if P2.passa_pela_janela(75,100,50,100,30) == False: testes += 1
        if P2.passa_pela_janela(20,22,5,20,10) == True: testes += 1
        if testes < 3:
            print('Funcao passa_pela_janela NÃO está OK')
        else:
            print('Funcao passa_pela_janela está OK')
        return(valor * (testes/3))
    except AttributeError:
        print('Funcao passa_pela_janela não foi encontrada')
        return(0)
    except Exception:
        print ('Funcao passa_pela_janela deu erro na execução')
        return(valor * (testes/3))

def nota_da_prova():
  soma =  teste_dias_premio()
  soma += teste_em_equilibrio()
  soma += teste_calcula_juros_compostos()
  soma += teste_carta_faltante()
  soma += teste_nome_curto()
  soma += teste_verifica_hora()
  soma += teste_ano_bissexto()
  soma += teste_passa_pela_janela()
  print("Seu somatorio de pontos:",soma)
  nota = min(10,soma)
  print("Sua nota é:",nota)


#nota_da_prova()
