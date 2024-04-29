#include <stdio.h>
#define Dim 105
#define INF 999999

int adj[Dim][Dim], adj2[Dim][Dim], distancia[Dim], visitado[Dim], cidades, rotas; 

int minimo (){
	int i, menor = INF, indice = -1;
	for(i = 1; i <= cidades; i++){
		if(distancia[i] < menor && !visitado[i]){
			menor = distancia[i];
			indice = i;
		}
	}
	return indice;
}

int quanto_custa(int origem, int destino, int escalas){
	int vertice, i, j, valido = 1, custo_total = 0;
	for(i = 1; i <= cidades; i++)
		for(j = 1; j <= cidades; j++)
			if((i == origem || i <= escalas || i == destino) && (j == destino || j <= escalas || j == origem) && (i != j))
				adj2[i][j] = adj[i][j];
	while(valido){
		vertice = minimo();
		if(vertice == -1){
			valido = 0;
		}else{
			if(vertice == destino){
				return distancia[destino];
			}else{
				visitado[vertice] = 1;
				for(i = 1; i <= cidades; i++)
					if(adj2[vertice][i] != -1 && !visitado[i] && distancia[i] > distancia[vertice] + adj2[vertice][i])
						distancia[i] = distancia[vertice] + adj2[vertice][i];
			}
		}
	}
	if(distancia[destino] == INF)
		return -1;
	else
		return distancia[destino];
}

int main(){
	int i, j, k, consultas, origem, destino, escalas, custo, instancias = 1;
	while(scanf("%d %d", &cidades, &rotas) != EOF){
		for(i = 0; i <= cidades; i++)
			for(j = 0; j <= cidades; j++)
				adj[i][j] = -1;
		for(i = 0; i < rotas; i++){
			scanf("%d %d %d", &origem, &destino, &custo);
			if(adj[origem][destino] == -1 || adj[origem][destino] > custo)
				adj[origem][destino] = custo;
		}
		scanf("%d", &consultas);
		printf("Instancia %d\n", instancias);
		instancias++;
		for(i = 0; i < consultas; i++){
			for(j = 0; j <= cidades; j++){
				for(k = 0; k <= cidades; k++)
					adj2[j][k] = -1;
				distancia[j] = INF;
				visitado[j] = 0;
			}
			scanf("%d %d %d", &origem, &destino, &escalas);
			distancia[origem] = 0;
			printf("%d\n", quanto_custa(origem, destino, escalas));
		}
		printf("\n");
	}
	return 0;
}
