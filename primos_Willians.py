import math as m

def fat(numero):
    if(numero == 0 or numero == 1):
        return 1
    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    return fatorial

for j in range(2, 1001):
    pi_n = -1
    for i in range(1, j+1):
        fatorial = (fat(i-1) + 1)%(2*i)
        valor = m.pi*(fatorial/i)
        pi_n += m.floor((m.cos(valor))**2)
    print(j, pi_n)
