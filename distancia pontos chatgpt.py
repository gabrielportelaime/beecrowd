import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pontos_mais_proximos(pontos):
    pontos_ord_x = sorted(pontos, key=lambda x: x[0])
    pontos_ord_y = sorted(pontos, key=lambda x: x[1])

    def encontrar_pontos_mais_proximos(pontos_ord_x, pontos_ord_y):
        n = len(pontos_ord_x)
        if n <= 3:
            return forca_bruta(pontos_ord_x)

        meio = n // 2
        ponto_meio = pontos_ord_x[meio]
        
        esquerda_x = pontos_ord_x[:meio]
        direita_x = pontos_ord_x[meio:]
        
        esquerda_y = []
        direita_y = []
        
        for ponto in pontos_ord_y:
            if ponto[0] < ponto_meio[0] or (ponto[0] == ponto_meio[0] and ponto[1] <= ponto_meio[1]):
                esquerda_y.append(ponto)
            else:
                direita_y.append(ponto)

        par_esquerda = encontrar_pontos_mais_proximos(esquerda_x, esquerda_y)
        par_direita = encontrar_pontos_mais_proximos(direita_x, direita_y)
        menor_distancia = min(dist(par_esquerda[0], par_esquerda[1]), dist(par_direita[0], par_direita[1]))
        par_meio = encontrar_pontos_mais_proximos_meio(pontos_ord_y, menor_distancia, ponto_meio)
        
        if par_meio is None:
            return par_esquerda
        else:
            return par_meio
        
    def encontrar_pontos_mais_proximos_meio(pontos_ord_y, menor_distancia, ponto_meio):
        melhores_pontos = None
        n = len(pontos_ord_y)
        for i in range(n):
            for j in range(i+1, n):
                if pontos_ord_y[j][1] - pontos_ord_y[i][1] > menor_distancia:
                    break
                
                distancia = dist(pontos_ord_y[i], pontos_ord_y[j])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    melhores_pontos = (pontos_ord_y[i], pontos_ord_y[j])

        return melhores_pontos
    
    def forca_bruta(pontos):
        n = len(pontos)
        if n < 2:
            return None
        
        melhor_distancia = dist(pontos[0], pontos[1])
        melhores_pontos = (pontos[0], pontos[1])
        
        for i in range(n):
            for j in range(i+1, n):
                distancia = dist(pontos[i], pontos[j])
                if distancia < melhor_distancia:
                    melhor_distancia = distancia
                    melhores_pontos = (pontos[i], pontos[j])
        
        return melhores_pontos
    
    return encontrar_pontos_mais_proximos(pontos_ord_x, pontos_ord_y)

while(True):
    pontos = []
    quantidade = int(input())
    if(quantidade == 0):
        break
    for i in range(quantidade):
        x, y = [float(coordenada) for coordenada in input().split()]
        pontos.append((x, y))
    par_pontos_proximos = pontos_mais_proximos(pontos)
    print("Pontos mais próximos:", par_pontos_proximos)
    print("Distancia: ", dist(par_pontos_proximos[0], par_pontos_proximos[1]))

