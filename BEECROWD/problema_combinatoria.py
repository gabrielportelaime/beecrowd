with open("valores.txt", "w") as arquivo:
    contador = 0
    for i in range(1, 101):
        contador_i = 0
        for j in range(i + 1, 101):
            for k in range(j + 1, 101):
                if(i + j + k == 120 and i != j and i != k and j != k):
                    tripla = '(' + str(i) + ', ' + str(j) + ', ' + str(k) + ')' + '\n'
                    arquivo.write(tripla)
                    contador += 1
                    contador_i += 1
        arquivo.write('---------------------------------------------------' + '\n')
        arquivo.write(str(contador_i) + '\n')
        arquivo.write('---------------------------------------------------' + '\n')
    arquivo.write(str(contador))
