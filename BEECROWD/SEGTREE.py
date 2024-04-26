vetor = [1, 2, 3, 4, 5]
tamanho = len(vetor)
arvore = [0]*(4*tamanho)

def constroi(no, l, r):
    if(l == r):
        arvore[no] = vetor[l]
        return
    meio = (l+r)//2
    constroi(2*no + 1, l, meio)
    constroi(2*(no + 1), meio+1, r)
    arvore[no] = arvore[2*no+1] + arvore[2*(no+1)]
    
def atualiza(posicao, valor, no, l, r):
    meio = (l+r)//2
    if(l == r):
        arvore[no] = valor
        return
    if(l <= posicao and meio >= posicao):
        atualiza(posicao, valor, 2*no+1, l, meio)
    else:
        atualiza(posicao, valor, 2*no+2, meio + 1, r)
    arvore[no] = arvore[2*no+1] + arvore[2*no+2]

constroi(0, 0, tamanho - 1)
print(arvore)
atualiza(4, 1, 0, 0, tamanho - 1)
print(arvore)