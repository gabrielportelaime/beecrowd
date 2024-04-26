while(True):
    try:
        partidas, gols = [int(x) for x in input().split()]
        saldos = []
        pontos = 0
        for i in range(partidas):
            marcado, tomado = [int(x) for x in input().split()]
            if(tomado == marcado):
                if(gols > 0):
                    gols -= 1
                    pontos += 3
                else:
                    pontos += 1
            elif(tomado > marcado):
                saldos.append(tomado - marcado)
            else:
                pontos += 3
        saldos.sort()
        for saldo in saldos:
            if(gols == saldo):
                pontos += 1
                gols -= saldo
            if(gols > saldo):
                pontos += 3
                gols -= (saldo + 1)
        print(pontos)
    except EOFError:
        break