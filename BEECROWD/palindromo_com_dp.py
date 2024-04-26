n = int(input())
lista = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
for i in range(n):
    s = input()
    t = len(s)
    dp = [[0] * t for _ in range(t)]
    for j in range(t):
        if s[j] in lista:
            dp[j][j] = 1
    maior = 1
    for j in range(t - 1, -1, -1):
        for k in range(j+1, t):
            if s[j] == s[k]:
                if k - j == 1 or dp[j+1][k - 1] == 1:
                    dp[j][k] = 1
                    if(k - j + 1) > maior:
                        maior = k - j + 1
    print(maior)
