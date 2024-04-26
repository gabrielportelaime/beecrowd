def calcular_asteriscos(expr):
    posicao = expr.find('*')
    while(posicao != -1):
        sem_fim = sem_comeco = False
        abre_chaves = expr.rfind('{', 0, posicao)
        fecha_chaves = expr.rfind('}', 0, posicao)
        antesde = abre_chaves
        if(abre_chaves == 0):
            sem_comeco = True
        conj1 = set(expr[abre_chaves + 1:fecha_chaves])
        abre_chaves = expr.find('{', posicao + 1, len(expr))
        fecha_chaves = expr.find('}', posicao + 1, len(expr))
        apartir = fecha_chaves
        if(fecha_chaves == len(expr) - 1):
            sem_fim = True
        conj2 = set(expr[abre_chaves + 1:fecha_chaves])
        sub_expr = conj1.intersection(conj2)
        if(sem_comeco and sem_fim):
            expr = '{' + ''.join(sub_expr) + '}'
        elif(sem_comeco):
            expr = '{' + ''.join(sub_expr) + '}' + expr[apartir + 1:]
        elif(sem_fim):
            expr = expr[:antesde] + '{' + ''.join(sub_expr) + '}'
        else:
            expr = expr[:antesde] + '{' + ''.join(sub_expr) + '}' + expr[apartir + 1:]
        posicao = expr.find('*')
    return expr

def calcular_com_parenteses(expr):
    while('(' in expr):
        fecha_parenteses = expr.find(')')
        abre_parenteses = expr.rfind('(', 0, fecha_parenteses)
        sub_expr = expr[abre_parenteses + 1:fecha_parenteses]
        resultado = calcular_asteriscos(sub_expr)
        expr = expr[:abre_parenteses] + str(resultado) + expr[fecha_parenteses + 1:]
    return calcular_asteriscos(expr)


while(True):
    try:
        entrada = input()
        resposta = '{' + ''.join(sorted(list(calcular_com_parenteses(entrada)[1:-1:]))) + '}'
        print(resposta)     
    except EOFError:
        break