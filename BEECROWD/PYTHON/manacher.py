def manacher(s):
    n = len(s)
    P = [0] * n
    C = R = 0  # Centro e borda direita do palíndromo mais à direita encontrado até o momento.

    for i in range(n):
        # Aproveitar simetria se i está dentro da borda direita atual.
        if i < R:
            mirror = 2 * C - i
            P[i] = min(R - i, P[mirror])

        # Expandir palíndromo centrado em i.
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while a < n and b >= 0 and s[a] == s[b]:
            P[i] += 1
            a += 1
            b -= 1

        # Atualizar centro e borda direita se necessário.
        if i + P[i] > R:
            C, R = i, i + P[i]

    return P

def generate_palindromic_substrings(s):
    n = len(s)
    result = []

    # Utilizando o array P gerado pelo algoritmo de Manacher.
    P = manacher(s)

    for i in range(n):
        # Adicionando substrings palindrômicas ímpares.
        result.append(s[i - P[i] : i + P[i] + 1])

        # Adicionando substrings palindrômicas pares.
        if i < n - 1 and s[i] == s[i + 1]:
            result.append(s[i - P[i] : i + P[i] + 2])

    return result

# Exemplo de uso:
string_exemplo = "babad"
resultado = generate_palindromic_substrings(string_exemplo)
print(resultado)
