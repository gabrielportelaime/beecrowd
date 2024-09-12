# ### ### ### ### ### ### ### ### ### ###
# ***   * *** *** * * *** *** *** *** ***
# * *   *   *   * * * *   *     * * * * *
# * *   * *** *** *** *** ***   * *** ***
# * *   * *     *   *   * * *   * * *   *
# ***   * *** ***   * *** ***   * *** ***

digitos = ["**** ** ** ****", "  *  *  *  *  *", "***  *****  ***", "***  ****  ****", "* ** ****  *  *", "****  ***  ****", "****  **** ****", "***  *  *  *  *", "**** ***** ****", "**** ****  ****"]

lista = []
for i in range(5):
    linha = input()
    tamanho = (len(linha) - 3)//4 + 1 
    espacos = 0
    for j in range(tamanho):
        if(i == 0):
            lista.append("")
        lista[j] += linha[espacos + 3*j:espacos + 3*(j+1)]
        espacos += 1

numero = ''
for i in range(len(lista)):
    numero += str(digitos.index(lista[i]))

if(int(numero)%6 == 0):
    print('BEER!!')
else:
    print('BOOM!!')