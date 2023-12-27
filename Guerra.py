quantidade = int(input())
quad = [int(x) for x in input().split()]
nlog = [int(x) for x in input().split()]
nlog.sort()
quad.sort()
resultado = 0
i = j = 0
while(i < quantidade and j < quantidade):
    if(quad[i] < nlog[j]):
        resultado += 1
        i += 1
        j += 1
    else:
        j += 1
        
print(resultado)