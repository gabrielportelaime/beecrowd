#include <stdio.h>
#define Dim 5000
#define Cid 105

int transmissoes[Dim][3], grafo[Cid] = {0}, conectadas = 0, cidades, linhas, certo;

int pertence(int vertice){
	int i;
	for(i = 0; i < conectadas; i++)
		if(grafo[i] == vertice)
			return 1;
	return 0;
}

int busca_linha(){
	int i, valido = 0, posicao_linha;
	for(i = 0; i < linhas; i++){
		if(!valido && transmissoes[i][2] && pertence(transmissoes[i][0]) && !pertence(transmissoes[i][1])){
			valido = certo = 1;
			posicao_linha = i;
		}else{
			if(!valido && transmissoes[i][2] && !pertence(transmissoes[i][0]) && pertence(transmissoes[i][1])){
				posicao_linha = i;
				certo = 0;
				valido = 1;
			}	
		}	
	}
	if(valido)
		return posicao_linha;
	else
		return -1;
}


int prim(){
	int aresta, Nacabou = 1;
	if(conectadas == 0){
		grafo[conectadas] = transmissoes[0][0];
		conectadas++;
	}
	while(cidades > conectadas && Nacabou){
		aresta = busca_linha();
		if(aresta < 0){
			Nacabou = 0;
		}else{
			if(certo)
				grafo[conectadas] = transmissoes[aresta][1];
			else
				grafo[conectadas] = transmissoes[aresta][0];
			conectadas++;
			transmissoes[aresta][2] = 0;
		}
	}
	if(Nacabou)
		return 1;
	else
		return 0;
}

int main(){
	int i, j, normal, teste = 1;
	scanf("%d %d", &cidades, &linhas);
	while(cidades != 0 && linhas != 0){
		for(i = 0; i < linhas; i++){
			for(j = 0; j < 2; j++)
				scanf("%d", &transmissoes[i][j]);
			transmissoes[i][2] = 1;
		}
		normal = prim();
		printf("Teste %d\n", teste);
		teste++;
		if(normal)
			printf("normal\n\n");
		else
			printf("falha\n\n");
		scanf("%d %d", &cidades, &linhas);
		for(i = 0; i < Cid; i++)
			grafo[i] = 0; 
		conectadas = 0;
	}	
}



