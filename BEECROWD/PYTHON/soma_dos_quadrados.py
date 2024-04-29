n, q = [int(x) for x in input().split()]

respostas = {}

for k in range(4):
    if(k == 1):
        if(int((n**(1/2)))**2 == n):
            respostas[1] = 'Yes'
        else:
            respostas[1] = 'No'
    elif(k == 2):
        acabou = False
        for j in range(1, int(n**(1/2)) + 1):
            complemento = n - j**2
            if(int(complemento**(1/2))**2 == complemento):
                respostas[2] = 'Yes'
                acabou = True
                break
        if(not acabou):
            respostas[2] = 'No'
    else:
        while(n%4 == 0):
            n = n//4
        if(n%8 == 7):
            respostas[3] = 'No'
        else:
            respostas[3] = 'Yes'

for i in range(q):
    k = int(input())
    if(k < 4):
        print(respostas[k])
    else:
        print('Yes')