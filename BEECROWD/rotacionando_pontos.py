import math as m

x, y, teta = [float(x) for x in input().split()]

x1 = x*m.cos(teta) - y*m.sin(teta)
y1 = y*m.cos(teta) + x*m.sin(teta)

print(x1, y1)