while True:
    dicionario = {}
    estudantes = int(input())
    if estudantes == 0:
        break
    vetor = []
    for _ in range(estudantes):
        soma = 0
        palavra = input()
        for j in range(len(palavra)):
            soma += ord(palavra[j])
        dicionario[palavra] = soma;
        vetor.append(palavra)
    menor = 0
    maior = estudantes
    while menor < maior:
        media = (maior + menor) // 2
        poder_a = 0
        multi_a = 1
        poder_b = 0
        for i in range(media, -1, -1):
            soma = dicionario[vetor[i]]*multi_a
            multi_a += 1
            poder_a += soma
        multi_a = 1
        for i in range(media + 1, estudantes):
            soma = dicionario[vetor[i]]*multi_a
            multi_a += 1
            poder_b += soma
        if poder_a == poder_b:
            print(vetor[media])
            break
        if poder_a > poder_b:
            maior = media
        if poder_a < poder_b:
            menor = media
        if menor == maior - 1:
            print("Impossibilidade de empate.")
            break
