joga, roda = [int(x) for x in input().split()]
rodadas = [int(x) for x in input().split()]
jogador = 0
pontos = 0
for i in range(joga):
    ponto_jogador = 0
    for j in range(roda):
        ponto_jogador += rodadas[j*joga + i]
    if(ponto_jogador >= pontos):
        pontos = ponto_jogador
        jogador = i + 1
print(jogador)