
import os, sys, io
from operator import xor
input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto):
    sys.stdout.write(str(texto) + "\n")

for i in range(0, 11):
    a = 9
    b = 6
    print(xor(a, i), end=' - ')
    print(xor(b, i), end=' - ')
    print(abs(xor(a, i) - xor(b, i)))

# for _ in range(int(input())):
#     a, b, r = map(int, input().split())
#     for i in range(0, r + 1):
#         d = abs(xor(a, i) - xor(b, i)) 
#         imprimir(d)