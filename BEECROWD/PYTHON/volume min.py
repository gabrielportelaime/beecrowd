from math import sqrt
while True:
    try:
        entrada = input().split()
        c, l = float(entrada[0]), float(entrada[1])
        soma = c+l
        produto = l*c
        funcao = [4, -2*(soma), produto]
        derivada = [12, soma*-2*2, produto]

        xDerivada = (-derivada[1] - sqrt( derivada[1]**2 - 4*derivada[0]*derivada[2] ))/(2*derivada[0])
        xFuncao = (funcao[1]*-1 - sqrt( funcao[1]**2 - 4*funcao[0]*funcao[2] ))/(2*funcao[0])
        print("%.3f 0.000 %.3f"%(xDerivada, xFuncao))
    except EOFError:
        break