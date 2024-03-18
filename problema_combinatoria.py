with open("valores.txt", "w") as arquivo:
    contador = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if(i + j + k == 120 and i != j and i != k and j != k):
                    tripla = '(' + str(i) + ', ' + str(j) + ', ' + str(k) + ')' + '\n'
                    arquivo.write(tripla)
                    contador += 1
    arquivo.write(str(contador))
