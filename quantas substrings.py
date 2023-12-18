import itertools

def findsubsets(s, n): 
    return set(itertools.combinations(s, n)) 

entrada = list(input())
string = []
resposta = set()

for i in range(len(entrada)):
    if(entrada[i] != "?"):
        string.append(entrada[i])
    else:
        for j in range(1, len(string) + 1):
            for k in findsubsets(string, j):
                resposta.add("".join(k))

print(resposta)