casa = trabalho = 0
atualc = atualt = 0
for i in range(int(input())):
    tempoc, tempot = input().split()
    if(tempoc == 'chuva'):
        if(atualc == 0):
            casa += 1
        else:
            atualc -= 1
        atualt += 1
    if(tempot == 'chuva'):
        if(atualt == 0):
            trabalho += 1
        else:
            atualt -= 1
        atualc += 1
print(casa, trabalho)


