while(True):
    a, d = [int(x) for x in input().split()]
    if(a == d == 0):
        break
    atacantes = [int(x) for x in input().split()]
    defensores = [int(x) for x in input().split()]
    atacantes.sort()
    defensores.sort()
    if(atacantes[0] < defensores[1]):
        print("Y")
    else:
        print("N")