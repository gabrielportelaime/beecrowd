class Arvore:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def intercepta(floresta, arvore_analisada):
    for arvore in floresta:
        if(arvore != arvore_analisada):
            delta = 4*((arvore.x+(arvore_analisada.y*arvore.y)/(arvore_analisada.x))**2)
            delta -= 4*(1+(arvore_analisada.y**2)/(arvore_analisada.x**2))*(arvore.x**2+arvore.y**2 - arvore.r**2)
            if(delta >= 0):
                return True
    return False

while(True):
    quantidade = int(input())
    floresta = []
    distancias = []
    if(quantidade == 0):
        break
    for i in range(quantidade):
        x, y, r = [int(x) for x in input().split()]
        floresta.append(Arvore(x, y, r))
    for arvore in floresta:
        if(not intercepta(floresta, arvore)):
            distancia = (arvore.x**2+arvore.y**2)**(1/2) - arvore.r
            distancias.append(distancia)
    print(min(distancias))