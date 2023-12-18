def suffix_array_alternative_naive(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

texto = 'gabriel'

for sufixo in suffix_array_alternative_naive(texto):
    print(texto[sufixo::])