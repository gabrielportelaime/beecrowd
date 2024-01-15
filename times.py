quantidade, qtd_times = [int(x) for x in input().split()]
pessoas = []
times = []
for i in range(qtd_times):
	times.append([])
for i in range(quantidade):
	nome, habilidade = input().split()
	habilidade = int(habilidade)
	pessoas.append([habilidade, nome])
pessoas.sort(reverse=True)
for i in range(quantidade):
	times[i%qtd_times].append(pessoas[i][1])
for i in range(qtd_times):
	times[i].sort()
	print("Time", i+1)
	for j in range(len(times[i])):
		print(times[i][j])
	print("")