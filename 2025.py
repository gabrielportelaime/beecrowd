for i in range(int(input())):
    frase = input().split(" ")
    for j in range(len(frase)):
        if("oulupukk" in frase[j] and 9 < len(frase[j]) < 12):
            frase[j] = "Joulupukki"
    print(" ".join(frase))