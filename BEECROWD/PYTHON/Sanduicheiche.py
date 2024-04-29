# while True:
#     try:
        
#     except EOFError:
#         break

entradas = "sanduicheiche\nbarrilarril\nratoato\nsol\ncoliseueu\nqueijoijo\nastroastro\na"
entradas = entradas.split('\n')

for entrada in entradas:
    palavra = entrada[-1]
    while(palavra in entrada[0:-len(palavra) - 1]):
        