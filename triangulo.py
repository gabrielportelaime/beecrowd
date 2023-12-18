def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

while(True):
    n, m = [int(x) for x in input().split()]
    pretos = []
    brancos = []
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        pretos.append([x, y])
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        brancos.append([x, y])
    soma = 0
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                x1, y1 = pretos[i]
                x2, y2 = pretos[j]
                x3, y3 = pretos[k]
                quantidade = 0
                for l in range(m):
                    x, y = brancos[l]
                    if(isInside(x1, y1, x2, y2, x3, y3, x, y)):
                        quantidade += 1
                soma += quantidade**2
    print(soma)