#include <stdio.h>

#define Dim 105
#define INF 999999

int matriz[Dim][Dim][Dim], cidades, rotas; 

int min(int a, int b){
	if(a < b)
		return a;
	return b;
}

void floyd (){
	int i, j, k;
	for(k = 1; k <= cidades; k++)
		for(i = 1; i <= cidades; i++)
			for(j = 1; j <= cidades; j++)
				matriz[i][j][k] = min(matriz[i][j][k-1], matriz[i][k][k-1] + matriz[k][j][k-1]);
}


int main(){
	int i, j, k, consultas, origem, destino, escalas, custo, instancias = 1, resultado;
	while(scanf("%d %d", &cidades, &rotas) != EOF){
		for(i = 0; i <= cidades; i++){
			for(j = 0; j <= cidades; j++){
				for(k = 0; k <= cidades; k++){
					if(i == j)
						matriz[i][j][k] = 0;
					else
						matriz[i][j][k] = INF;
				}
			}
		}
		for(i = 0; i < rotas; i++){
			scanf("%d %d %d", &origem, &destino, &custo);
			if(matriz[origem][destino][0] == INF || matriz[origem][destino][0] > custo)
				matriz[origem][destino][0] = custo;
		}
		scanf("%d", &consultas);
		printf("Instancia %d\n", instancias);
		instancias++;
		floyd();
		for(i = 0; i < consultas; i++){
			scanf("%d %d %d", &origem, &destino, &escalas);
			if(matriz[origem][destino][escalas] == INF)
				resultado = -1;
			else
				resultado = matriz[origem][destino][escalas];
			printf("%d\n", resultado);
		}
		printf("\n");
	}
	return 0;
}

