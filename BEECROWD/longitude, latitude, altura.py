import math

pi = math.pi
raio = 6378
contador = 1

def radiano(graus):
    return 2*(pi/360)*graus

def distancia(x1, y1, z1, x2, y2, z2):
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**(1/2)

entrada = True
while(True):
    if(entrada):
        n, la, lo, h = [float(x) for x in input().split()]
    entrada = True
    n = int(n)
    if(n == 0):
        break
    p = h + raio
    la = radiano(la)
    lo = radiano(lo)
    t = ((p)**2-(raio)**2)**(1/2)
    p0x = p*math.cos(lo)*math.cos(la)
    p0y = p*math.sin(lo)*math.cos(la)
    p0z = p*math.sin(la)
    print("Test case " + str(contador) + ":")
    contador += 1
    for i in range(n):
        lista = input().split()
        if(len(lista) > 3):
            nome, la, lo, n, la, lo, h = lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]
            entrada = False
        else:
            nome, la, lo = lista[0], lista[1], lista[2]
        la = float(la)
        lo = float(lo)
        la = radiano(la)
        lo = radiano(lo)
        p1x = raio*math.cos(lo)*math.cos(la)
        p1y = raio*math.sin(lo)*math.cos(la)
        p1z = raio*math.sin(la)
        d = distancia(p0x, p0y, p0z, p1x, p1y, p1z)
        if(d < t):
            print(nome)
        