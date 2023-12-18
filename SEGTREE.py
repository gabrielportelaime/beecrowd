# IMPLEMENTAÇÃO DE UMA SEGTREE

vetor = [1,2,4,3,5,10]
tamanho = len(vetor)
arvore = [0]*(4*tamanho)

def build(node, l, r):
    if(l == r):
        arvore[node] = vetor[l]
        return
    mid = (l+r)//2
    build(2*node + 1, l, mid)
    build(2*(node + 1), mid+1, r)
    arvore[node] = arvore[2*node+1] + arvore[2*(node+1)]

build(0, 0, tamanho-1)

print(arvore)