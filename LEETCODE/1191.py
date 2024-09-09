class Solution:
    def solu(self, arr, k) -> int:
        soma = ultimo = 0
        todos = True
        for elemento in arr:
            if(elemento < 0):
                if(soma > ultimo):
                    ultimo = soma
                    soma = 0
                todos = False
                continue
            else:
                soma += elemento
        inicio = 0
        final = len(arr) - 1
        soma = 0
        verifica = True
        while(verifica):
            verifica = False
            if(arr[inicio] >= 0):
                soma += arr[inicio]
                inicio += 1
                verifica = True
            if(arr[final] >= 0):
                soma += arr[final]
                final -= 1
                verifica = True
        maior = max(ultimo, soma)%(10**9 + 7)
        if(sum(arr) > 0):
            return max(maior, sum(arr)*k)
        else:
            return maior
lista = [-5,-2,0,0,3,9,-2,-5,4]
k = 5
solucao = Solution()
print(solucao.solu(lista, k))