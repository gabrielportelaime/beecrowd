#include <stdio.h>
#define Dim 4955
#define Cid 100
#define INF 999999

int fios[Dim][3], grafo[Cid] = {0}, conectadas = 0, custo_total = 0, tabas, ligacoes, certo;

int pertence(int vertice){
	int i;
	for(i = 0; i < conectadas; i++)
		if(grafo[i] == vertice)
			return 1;
	return 0;
}

int busca_menor_ligacao(){
	int i, menor = INF, posicao_ligacao;
	for(i = 0; i < ligacoes; i++){
		if(fios[i][2] < menor && fios[i][2] != 0 && pertence(fios[i][0]) && !pertence(fios[i][1])){
			menor = fios[i][2];
			posicao_ligacao = i;
			certo = 1;
		}else{
			if(fios[i][2] < menor && fios[i][2] != 0 && !pertence(fios[i][0]) && pertence(fios[i][1])){
				menor = fios[i][2];
				posicao_ligacao = i;
				certo = 0;
			}	
		}	
	}
	return posicao_ligacao;
}


int prim(){
	int menor_aresta;
	if(conectadas == 0){
		grafo[conectadas] = fios[0][0];
		conectadas++;
	}
	while(tabas > conectadas){
		menor_aresta = busca_menor_ligacao();
		if(certo)
			grafo[conectadas] = fios[menor_aresta][1];
		else
			grafo[conectadas] = fios[menor_aresta][0];
		conectadas++;
		custo_total += fios[menor_aresta][2];
		fios[menor_aresta][2] = 0;
	}
	return custo_total;
}

int main(){
	int i, j, custo, teste = 1;
	scanf("%d %d", &tabas, &ligacoes);
	while(tabas != 0 && ligacoes != 0){
		for(i = 0; i < ligacoes; i++)
			for(j = 0; j < 3; j++)
				scanf("%d", &fios[i][j]);
		custo = prim();
		printf("Teste %d\n", teste);
		teste++;
		for(i = 0; i < ligacoes; i++)
			if(fios[i][2] == 0)
				printf("%d %d\n", fios[i][0], fios[i][1]);
		printf("\n");
		scanf("%d %d", &tabas, &ligacoes);
		for(i = 0; i < Cid; i++)
			grafo[i] = 0; 
		conectadas = custo_total = 0;
	}	
}



