import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def dist(p1, p2):
	return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def bruteForce(P, n):
	min = float('inf')
	for i in range(n):
		for j in range(i+1, n):
			if dist(P[i], P[j]) < min:
				min = dist(P[i], P[j])
	return min

def stripClosest(strip, size, d):
	min = d 
	for i in range(size):
		for j in range(i+1, size):
			if (strip[j].y - strip[i].y) < min:
				if dist(strip[i],strip[j]) < min:
					min = dist(strip[i], strip[j])
	return min

def closestUtil(Px, Py, n):
	if n <= 3:
		return bruteForce(Px, n)
	mid = n // 2
	midPoint = Px[mid]
	Pyl = [] 
	Pyr = []
	li = ri = 0 
	for i in range(len(Py)):
		if((Py[i].x < midPoint.x or (Py[i].x == midPoint.x and Py[i].y < midPoint.y)) and li < mid):
			Pyl.append(Py[i])
			li += 1
		else:
			Pyr.append(Py[i])
			ri += 1
	dl = closestUtil(Px, Pyl, mid)
	dr = closestUtil(Px[mid:], Pyr, n-mid)
	d = min(dl, dr)
	strip = [None] * n
	j = 0
	for i in range(n):
		if abs(Py[i].x - midPoint.x) < d:
			strip[j] = Py[i]
			j += 1
	return stripClosest(strip, j, d)

def closest(P, n):
	Px = sorted(P, key = lambda a : a.x)
	Py = sorted(P, key = lambda a : a.y)
	return closestUtil(Px, Py, n)

while(True):
    quantidade = int(input())
    if(quantidade == 0):
        break
    P = []
    lista = []
    for i in range(quantidade):
        Px, Py = [float(x) for x in input().split()]
        if(Px in lista):
            Px += 0.01
        P.append(Point(Px, Py))
        lista.append(Px)
    distancia = closest(P, len(P))
    if(distancia >= 10000):
        print("INFINITY")
    else:
        print("{0:.4f}".format(distancia))
