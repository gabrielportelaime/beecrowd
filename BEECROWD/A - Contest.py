for i in range(int(input())):
    pao, queijo, presunto = [int(x) for x in input().split()]
    if(pao - 1 <= queijo+presunto):
        print(pao*2-1)
    else:
        print((queijo+presunto)*2+1)