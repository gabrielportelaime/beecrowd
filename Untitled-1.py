import math

for i in range(int(input())):
    pessoas, total = [int(x) for x in input().split()]
    volume = total/pessoas
    base_menor, base_maior, altura = [int(x) for x in input().split()]
    if(base_maior == base_menor):
        area_base = (math.pi)*(base_maior**2)
        resposta = volume/area_base
    else:
        razao = (base_maior-base_menor)/altura
        raiz = (((3*volume)/(math.pi))*razao + base_menor**3)**(1/3)
        resposta = (raiz-base_menor)/razao
    print(f"{resposta:.2f}")
