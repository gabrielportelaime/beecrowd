for i in range(int(input())):
    frase = input().split(" ")
    for palavra in frase:
        if("oulupukk" in palavra and (len(palavra) == 10 or (len(palavra) > 10 and palavra[-1] == "."))):
            frase[frase.index(palavra)] = "Joulupukki"
    print(' '.join(frase))