for quantidade in range(18, 19):
    validado = list(range(1, quantidade + 1))
    i = 600000000
    while(True):
        todos = list(range(1, 2*quantidade + 1))
        desc = 0
        for j in range(quantidade):
            tamanho = len(todos)
            pos = (i + desc - 1)%tamanho
            todos.pop(pos)
            desc = pos
        if(todos == validado):
            valor = i
            break
        i += 1
        if(i%1000000 == 0):
            print(i)
    print("Resultado: ", valor)
