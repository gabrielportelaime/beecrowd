quantidade = int(input())
linhas = 0
while True:
    try:
        mensagem = input()
        if(len(mensagem) > quantidade):
            while(len(mensagem) > quantidade):
                if(mensagem[0] == ' '):
                    mensagem = mensagem[1::]
                linhas += 1
                if(len(mensagem) > quantidade):
                    mensagem = mensagem[quantidade::]
            if(len(mensagem) > 0):
                linhas += 1
        elif(mensagem != '\n' and mensagem != ''):
            linhas += 1
    except EOFError:
        break
print(linhas)

