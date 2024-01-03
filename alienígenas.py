class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    distancia = (p1.x-p2.x)**2+(p1.y-p2.y)**2
    return distancia**(1/2)

def determinante(matriz):
    det = (matriz[0][0]*matriz[1][1]*matriz[2][2])
    det += (matriz[0][1]*matriz[1][2]*matriz[2][0])
    det += (matriz[0][2]*matriz[1][0]*matriz[2][1])
    det -= (matriz[2][0]*matriz[1][1]*matriz[0][2])
    det -= (matriz[2][1]*matriz[1][2]*matriz[0][0])
    det -= (matriz[2][2]*matriz[0][1]*matriz[1][0])
    return det

def substitui(matriz, lista, coluna):
    retorno = []
    for i in range(3):
        linha = []
        if(coluna == 0):
            linha.append(lista[i])
            linha.append(matriz[i][1])
            linha.append(matriz[i][2])
        if(coluna == 1):
            linha.append(matriz[i][0])
            linha.append(lista[i])
            linha.append(matriz[i][2])
        if(coluna == 2):
            linha.append(matriz[i][0])
            linha.append(matriz[i][1])
            linha.append(lista[i])
        retorno.append(linha)
    return retorno

def calc_circun(p1, p2, p3):
    resulta = -((p1.x**2)+(p1.y**2))
    resultb = -((p2.x**2)+(p2.y**2))
    resultc = -((p3.x**2)+(p3.y**2))
    resultado = [resulta, resultb, resultc]
    lista = []
    lista.append([2*p1.x, 2*p1.y, 1])
    lista.append([2*p2.x, 2*p2.y, 1])
    lista.append([2*p3.x, 2*p3.y, 1])
    det = determinante(lista)
    deta = determinante(substitui(lista, resultado, 0))
    detb = determinante(substitui(lista, resultado, 1))
    detc = determinante(substitui(lista, resultado, 2))
    if(det != 0):
        a = deta/det
        b = detb/det
        c = detc/det
        return [-a, -b, (a**2+b**2-c)]
    else:
        d1 = dist(p1, p2)
        d2 = dist(p1, p3)
        d3 = dist(p2, p3)
        if(d2 < d1 > d3):
            centrox = (p1.x+p2.x)/2
            centroy = (p1.y+p2.y)/2
            raio = d1/2
        elif(d1 < d2 > d3):
            centrox = (p1.x+p3.x)/2
            centroy = (p1.y+p3.y)/2
            raio = d2/2
        elif(d1 < d3 > d2):
            centrox = (p3.x+p2.x)/2
            centroy = (p3.y+p2.y)/2
            raio = d3/2
        return [centrox, centroy, raio**2]

def dentro(circunferencia, humano):
    distancia = (humano.x-circunferencia[0])**2 + (humano.y-circunferencia[1])**2
    if(distancia <= circunferencia[2]):
        return True
    return False

while(True):
    n, m = [int(x) for x in input().split()]
    if(n == 0 and m == 0):
        break
    maximo = -1
    aliens = []
    humanos = []
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        aliens.append(Ponto(x, y))
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        humanos.append(Ponto(x, y))
    for i in range(0, n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                circunferencia = calc_circun(aliens[i], aliens[j], aliens[k])
                verifica = True
                for humano in humanos:
                    if(dentro(circunferencia, humano)):
                        verifica = False
                        break
                conta = 0
                if(verifica):
                    for alien in aliens:
                        if(dentro(circunferencia, alien)):
                            conta += 1
                    if(conta > maximo):
                        maximo = conta
    if(maximo == -1):
        print("2")
    else:
        print(maximo)