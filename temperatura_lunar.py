quantidade, intervalo = [int(x) for x in input().split()]
teste = 1

while(intervalo != 0 and quantidade != 0):
    medias = []
    somas = [0]
    soma = 0
    for i in range(quantidade):
        soma += int(input())
        somas.append(soma)
    for i in range(quantidade - intervalo + 1):
        media = int((somas[i + intervalo] - somas[i])/intervalo)
        medias.append(media)
    print("Teste", teste)
    teste += 1
    print(min(medias), max(medias), end="\n\n")
    quantidade, intervalo = [int(x) for x in input().split()]