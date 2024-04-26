entrada = "pwwkew"
maximo = ultima_pos = contador = 0
contem = {}
for i in range(len(entrada)):
    if(contem.get(entrada[i]) is None):
        contem[entrada[i]] = i
        contador += 1
    else:
        pos_atual = contem.get(entrada[i])
        if(pos_atual > ultima_pos):
            ultima_pos = pos_atual
        contem[entrada[i]] = i
        contador = i - ultima_pos
    if(contador > maximo):
            maximo = contador
print(maximo)