#include <stdio.h>
#define Dim 19805
#define Cid 100
#define INF 999999

int ferro[Dim][3], rodo[Dim][3], grafo[Cid] = {0}, conectadas = 0, custo_total = 0, cidades, ferrovias, rodovias, certo;

int pertence(int vertice){
	int i;
	for(i = 0; i < conectadas; i++)
		if(grafo[i] == vertice)
			return 1;
	return 0;
}

int busca_menor_ferrovia(){
	int i, menor = INF, posicao_aresta;
	for(i = 0; i < ferrovias; i++){
		if(ferro[i][2] < menor && ferro[i][2] != 0 && pertence(ferro[i][0]) && !pertence(ferro[i][1])){
			menor = ferro[i][2];
			posicao_aresta = i;
			certo = 1;
		}else{
			if(ferro[i][2] < menor && ferro[i][2] != 0 && !pertence(ferro[i][0]) && pertence(ferro[i][1])){
				menor = ferro[i][2];
				posicao_aresta = i;
				certo = 0;
			}	
		}	
	}
	if(menor == INF)
		return -1;
	else
		return posicao_aresta;
}

int busca_menor_rodovia(){
	int i, menor = INF, posicao_aresta;
	for(i = 0; i < rodovias; i++){
		if(rodo[i][2] < menor && rodo[i][2] != 0 && pertence(rodo[i][0]) && !pertence(rodo[i][1])){
			menor = rodo[i][2];
			posicao_aresta = i;
			certo = 1;
		}else{
			if(rodo[i][2] < menor && rodo[i][2] != 0 && !pertence(rodo[i][0]) && pertence(rodo[i][1])){
				menor = rodo[i][2];
				posicao_aresta = i;
				certo = 0;
			}	
		}	
	}
	return posicao_aresta;
}

int prim(){
	int menor_aresta;
	if(conectadas == 0){
		grafo[conectadas] = ferro[0][0];
		conectadas++;
	}
	while(cidades > conectadas){
		menor_aresta = busca_menor_ferrovia();
		if(menor_aresta < 0){
			menor_aresta = busca_menor_rodovia();
			if(certo)
				grafo[conectadas] = rodo[menor_aresta][1];
			else
				grafo[conectadas] = rodo[menor_aresta][0];
			conectadas++;
			custo_total += rodo[menor_aresta][2];
			rodo[menor_aresta][2] = 0;
		}else{
			if(certo)
				grafo[conectadas] = ferro[menor_aresta][1];
			else
				grafo[conectadas] = ferro[menor_aresta][0];
			conectadas++;
			custo_total += ferro[menor_aresta][2];
			ferro[menor_aresta][2] = 0;
		}
	}
	return custo_total;
}

int main(){
	int i, j, custo;
	scanf("%d %d %d", &cidades, &ferrovias, &rodovias);
	for(i = 0; i < ferrovias; i++)
		for(j = 0; j < 3; j++)
			scanf("%d", &ferro[i][j]);
	for(i = 0; i < rodovias; i++)
		for(j = 0; j < 3; j++)
			scanf("%d", &rodo[i][j]);
	custo = prim();
	printf("%d\n", custo);
}



