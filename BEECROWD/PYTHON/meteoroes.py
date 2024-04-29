x1, y1, x2, y2 = [int(x) for x in input().split()]
parou = (x1 == 0) and (x2 == 0) and (y1 == 0) and (y2 == 0)
teste = 1
while(not parou):
    quantidade = 0
    for i in range(int(input())):
        xm, ym = [int(x) for x in input().split()]
        if(x1 <= xm <= x2 and y2 <= ym <= y1):
            quantidade += 0
    print("Teste", teste)
    print(quantidade)
    teste += 1
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    parou = (x1 == 0) and (x2 == 0) and (y1 == 0) and (y2 == 0)