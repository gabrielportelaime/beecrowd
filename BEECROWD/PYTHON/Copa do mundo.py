while(True):
    times, partidas = [int(x) for x in input().split()]
    if(times == partidas == 0):
        break
    soma = 0
    for _ in range(times):
        nome, pontuacao = input().split()
        pontuacao = int(pontuacao)
        soma += pontuacao
    print(3*partidas - soma)