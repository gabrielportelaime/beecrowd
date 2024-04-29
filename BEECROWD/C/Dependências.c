#include <stdio.h>
#define Dim 105

int dependencias[Dim][Dim], n, guardado[Dim], visitado[Dim];

int retorna_dependencias(int filho){
	int i, diretas = 0, indiretas = 0;
	if(guardado[filho] && !visitado[filho])
		return guardado[filho];
	for(i = 0; i < n; i++){
		if(dependencias[filho][i] && !visitado[i]){
			visitado[i] = 1;
			diretas++;
			indiretas += retorna_dependencias(i);
		}
	}
	guardado[filho] = diretas+indiretas;
	return diretas+indiretas;	
}

int main(){
	int i, j, quantidade, filho, maior, numero, calculo;
	scanf("%d", &n);
	while(n){
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				dependencias[i][j] = guardado[i] = 0;	
		for(i = 0; i < n; i++){
			scanf("%d", &quantidade);
			for(j = 0; j < quantidade; j++){
				scanf("%d", &filho);	
				dependencias[i][filho-1] = 1;
			}
		}
		maior = -1;
		for(i = 0; i < n; i++){
			for(j = 0; j < n; j++)
				visitado[j] = 0;
			calculo = retorna_dependencias(i);
			if(maior < calculo){
				maior = calculo;
				numero = i+1;
			}
		}
		printf("%d\n", numero);
		scanf("%d", &n);
	}
	return 0;
}
