def palindromo(palavra):
    tamanho = len(palavra)
    for i in range(tamanho//2):
        if(palavra[i] != palavra[tamanho - i - 1]):
            return False
    return True

def substrings(string):
    n = len(string)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(string[i:j])
    return result

quantidade = int(input())
minha_string = input()
todas_as_substrings = substrings(minha_string)
lista_ordenada = sorted(todas_as_substrings, key=len, reverse=True)
print(lista_ordenada)

for palavra in lista_ordenada:
    if(palindromo(palavra)):
        print(len(palavra))
        break