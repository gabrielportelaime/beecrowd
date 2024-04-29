def calcular_sem_parenteses(expr):
    for operacao in ['*', '+-']:
        operacao_real = operacao
        if(operacao_real == '+-'):
            mais = expr.find('+')
            menos = expr.find('-')
            if(mais != -1 and menos != -1):
                if(mais < menos):
                    operacao_real = '+'
                    posicao = mais
                else:
                    operacao_real = '-'
                    posicao = menos
            elif(mais != -1):
                operacao_real = '+'
                posicao = mais
            else:
                operacao_real = '-'
                posicao = menos
        else:
            posicao = expr.find(operacao_real)
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
            if(operacao_real == '*'):
                sub_expr = conj1.intersection(conj2)
            if(operacao_real == '+'):
                sub_expr = conj1.union(conj2)
            if(operacao_real == '-'):
                sub_expr = conj1.difference(conj2)
            if(sem_comeco and sem_fim):
                expr = '{' + ''.join(sub_expr) + '}'
            elif(sem_comeco):
                expr = '{' + ''.join(sub_expr) + '}' + expr[apartir + 1:]
            elif(sem_fim):
                expr = expr[:antesde] + '{' + ''.join(sub_expr) + '}'
            else:
                expr = expr[:antesde] + '{' + ''.join(sub_expr) + '}' + expr[apartir + 1:]
            operacao_real = operacao
            if(operacao_real == '+-'):
                mais = expr.find('+')
                menos = expr.find('-')
                if(mais != -1 and menos != -1):
                    if(mais < menos):
                        operacao_real = '+'
                        posicao = mais
                    else:
                        operacao_real = '-'
                        posicao = menos
                elif(mais != -1):
                    operacao_real = '+'
                    posicao = mais
                else:
                    operacao_real = '-'
                    posicao = menos
            else:
                posicao = expr.find(operacao_real)
    return expr

def calcular_com_parenteses(expr):
    while('(' in expr):
        fecha_parenteses = expr.find(')')
        abre_parenteses = expr.rfind('(', 0, fecha_parenteses)
        sub_expr = expr[abre_parenteses + 1:fecha_parenteses]
        resultado = calcular_sem_parenteses(sub_expr)
        expr = expr[:abre_parenteses] + str(resultado) + expr[fecha_parenteses + 1:]
    return calcular_sem_parenteses(expr)


while(True):
    try:
        entrada = input()
        resposta = '{' + ''.join(sorted(list(calcular_com_parenteses(entrada)[1:-1:]))) + '}'
        print(resposta)     
    except EOFError:
        break