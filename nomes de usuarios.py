while True:
    try:
        entrada = input().split()
        alunos = int(entrada[0])
        ano = entrada[1]
        users = []
        quantidade = 0
        for i in range(alunos):
            nomes = input().split()
            user = ""
            for nome in nomes:
                user += nome[0]
            if(user not in users):
                users.append(user)
            else:
                quantidade += 1
        print(quantidade)
    except EOFError:
        break