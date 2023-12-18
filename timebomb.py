numeros = []

traducao = {"**** ** ** ****":'0',"  *  *  *  *  *":'1',"***  *****  ***":'2',"***  ****  ****":'3',"* ** ****  *  *":'4',
    "****  ***  ****":'5',"****  **** ****":'6',"***  *  *  *  *":'7',"**** ***** ****":'8',"**** ****  ****":'9'
}

for i in range(5):
    linha = input()
    for j in range(len(linha)//4):
        numero = linha[j*4] + linha[j*4 + 1] + linha[j*4 + 2]
        if(i == 0):
            numeros.append(numero)
        else:
            numeros[i] += numero

num = ""

for numero in numeros:
    num += traducao[numero]

print(num)