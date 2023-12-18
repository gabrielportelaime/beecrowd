palavra = input()
distancia = int(input())
palavra1 = input()
palavra2 = input()
palavra3 = input()
palavra4 = input()
palavra5 = input()

distancia1 = distancia2 = distancia3 = distancia4 = distancia5 = 0

for i in range(len(palavra)):
    if(palavra[i] != palavra1[i]):
        distancia1 += 1
    if(palavra[i] != palavra2[i]):
        distancia2 += 1
    if(palavra[i] != palavra3[i]):
        distancia3 += 1
    if(palavra[i] != palavra4[i]):
        distancia4 += 1
    if(palavra[i] != palavra5[i]):
        distancia5 += 1

minimo = min(distancia1, distancia2, distancia3, distancia4, distancia5)

if(minimo > distancia):
    print("-1")
else:
    if(distancia1 == minimo):
        print("1")
    elif(distancia2 == minimo):
        print("2")
    elif(distancia3 == minimo):
        print("3")
    elif(distancia4 == minimo):
        print("4")
    elif(distancia5 == minimo):
        print("5")
    print(minimo)



