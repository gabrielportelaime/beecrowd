import math

contador = 1
while(True):
    r, n = [int(x) for x in input().split()]
    if(r == n == 0):
        break
    sufixos = math.ceil(r/n)
    print("Case " + str(contador) + ":", end=' ')
    if(sufixos > 27):
        print("impossible")
    else:
        print(sufixos - 1)
    contador += 1