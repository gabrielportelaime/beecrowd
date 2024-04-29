respostas = []

for i in range(int(input())):
    cartas = list(input())
    if("A" in cartas and "K" in cartas and "J" in cartas and "Q" in cartas):
        respostas.append("Aaah muleke")
    else:
        respostas.append("Ooo raca viu")

print('\n'.join(respostas))