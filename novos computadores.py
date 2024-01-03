while(True):
    n = int(input())
    if(n == 0):
        break
    maxx = [9999, -9999]
    minx = [9999, -9999]
    minimox = 9999
    maximox = -9999
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        if(x < minimox):
            minimox
            if(y < minx[0]):
                minx[0] = y
            if(y > minx[1]):
                minx[1] = y
        if(x > maximox):
            if(y < maxx[0]):
                maxx[0] = y
            if(y > maxx[1]):
                maxx[1] = y
        