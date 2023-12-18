import math

pi = math.pi

while(True):
    try:
        lado = float(input())
        Ac = (lado**2)*(pi/12 - 1/4 + ((3**(1/2) - 1)**2)/8)*4
        Af = 2*(2*((lado**2)*(pi/4 - 1/2)) - Ac)
        Ar = lado**2 - Ac- Af
        print(f"{Ac:.3f} {Af:.3f} {Ar:.3f}")
    except EOFError:
        break