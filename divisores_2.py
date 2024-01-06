numero = int(input())
divisores = [1]
for i in range(2, int((numero)**(1/2)) + 1):
	if(numero%i == 0):
		divisores.append(i)
		divisores.append(numero//i)
divisores.sort()
divisores.append(numero)
[print(i, end=" ") for i in divisores]