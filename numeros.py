def alga_dif(numero, quantidade):
    if(len(set(numero)) - len(numero) <= quantidade):
        return True
    return False

contador = 0
for i in range(100, 1001):
    if(alga_dif(str(i), 0)):
        continua = True
        numero = str(i)
        print(i, "- Algarimos diferentes!")
        while(continua):
            asc = list(numero)
            asc.sort()
            desc = list(numero)
            desc.sort(reverse=True)
            resultado = str(int("".join(desc)) - int("".join(asc)))
            print("".join(asc), "".join(desc), resultado)
            if resultado == "495":
                continua = False
            else:
                numero = resultado
        contador += 1
print(contador)