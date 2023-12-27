import os, sys, io
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

quantidade = int(input())
while(quantidade != 0):
    for i in range(quantidade):
        q_trap, b1, b2 = [float(x) for x in input().split()]
        area = (5 * (b1 + b2)) / 2
        area = area*q_trap
        imprimir("Size #" + str(i + 1) + ":")
        imprimir(f"Ice Cream Used: {area:.2f} cm2")
    quantidade = int(input())
    imprimir("")