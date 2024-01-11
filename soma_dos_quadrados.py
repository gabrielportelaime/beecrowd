n, q = [int(x) for x in input().split()]

for i in range(q):
    k = int(input())
    if(k < 4):
        if(k == 1):
            if(int((n**(1/2)))**2 == n):
                print('Yes')
            else:
                print('No')
        elif(k == 2):
            acabou = False
            for j in range(1, int(n**(1/2)) + 1):
                complemento = n - j**2
                if(int(complemento**(1/2))**2 == complemento):
                    print('Yes')
                    acabou = True
                    break
            if(not acabou):
                print('No')
        else:
            while(n%4 == 0):
                n = n//4
            if(n%8 == 7):
                print('No')
            else:
                print('Yes')
    else:
        print('Yes')