class Quadrado:
    def __init__(self, xc, yc, l):
        self.vertices = [(xc+l/2, yc+l/2), (xc-l/2, yc+l/2), (xc+l/2, yc-l/2), (xc-l/2, yc-l/2)]
        self.xc = xc
        self.yc = yc
        self.l = l

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1] - b[1])**2)**(1/2)

def isDentro(q1, q2):
    for vertice in q1.vertices:
        dentrox = q2.xc - q2.l/2 <= vertice[0] <= q2.xc + q2.l/2
        dentroy = q2.yc - q2.l/2 <= vertice[1] <= q2.yc + q2.l/2
        if(dentrox and dentroy):
            return True
    return False

def distanciaMin(q1, q2):
    distancia_minima = float('inf')
    if((q2.xc > q1.xc + q1.l/2 + q2.l/2) and (q1.yc - q1.l/2 - q2.l/2 <= q2.yc <= q1.yc + q1.l/2 + q2.l/2)):
        distancia_minima = q2.xc - q1.xc - q1.l/2 - q2.l/2
    elif((q2.xc < q1.xc - q1.l/2 - q2.l/2) and (q1.yc - q1.l/2 - q2.l/2 <= q2.yc <= q1.yc + q1.l/2 + q2.l/2)):
        distancia_minima = q1.xc - q2.xc - q1.l/2 - q2.l/2
    elif((q2.yc > q1.yc + q1.l/2 + q2.l/2) and (q1.xc - q1.l/2 - q2.l/2 <= q2.xc <= q1.xc + q1.l/2 + q2.l/2)):
        distancia_minima = q2.yc - q1.yc - q1.l/2 - q2.l/2
    elif((q2.yc < q1.yc - q1.l/2 - q2.l/2) and (q1.xc - q1.l/2 - q2.l/2 <= q2.xc <= q1.xc + q1.l/2 + q2.l/2)):
        distancia_minima = q1.yc - q2.yc - q1.l/2 - q2.l/2
    elif((q2.xc > q1.xc + q1.l/2 + q2.l/2) and (q2.yc > q1.yc + q1.l/2 + q2.l/2)):
        distancia_minima = dist(q1.vertices[0], q2.vertices[3])
    elif((q2.xc > q1.xc + q1.l/2 + q2.l/2) and (q2.yc < q1.yc - q1.l/2 - q2.l/2)):
        distancia_minima = dist(q1.vertices[2], q2.vertices[1])
    elif((q2.xc < q1.xc - q1.l/2 - q2.l/2) and (q2.yc > q1.yc + q1.l/2 + q2.l/2)):
        distancia_minima = dist(q1.vertices[1], q2.vertices[2])
    elif((q2.xc < q1.xc - q1.l/2 - q2.l/2) and (q2.yc < q1.yc - q1.l/2 - q2.l/2)):
        distancia_minima = dist(q1.vertices[3], q2.vertices[0])
    return distancia_minima

andares, horizontal = [int(x) for x in input().split()]
quadrados = []
possivel = True
for i in range(andares):
    xc, yc, l = [int(x) for x in input().split()]
    quadrados.append(Quadrado(xc, yc, l))
    if(i > 0):
        if(not isDentro(quadrados[i], quadrados[i-1]) and not isDentro(quadrados[i-1], quadrados[i])):
            if(distanciaMin(quadrados[i], quadrados[i-1]) > horizontal):
                possivel = False

if(possivel):
    print("YEAH")
else:
    print("OUCH")