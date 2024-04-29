#include <stdio.h>
#define Dim 1005

int comprimento_total, quantidade_frases, frases[Dim][2], guardado[Dim][Dim];

int max (int a, int b){
	if(a >= b)
		return a;
	else
		return b;
}

int mochila (int comprimento_disponivel, int i){
	int a, b, resultado;
	if(guardado[comprimento_disponivel][i]){
		return guardado[comprimento_disponivel][i];
	}else{
		if(i >= quantidade_frases || comprimento_disponivel == 0){
			resultado = 0;
		}else{
			if(frases[i][0] > comprimento_disponivel){
				resultado = mochila(comprimento_disponivel, i+1);
			}else{
				a = mochila(comprimento_disponivel, i+1);
				b = frases[i][1] + mochila(comprimento_disponivel - frases[i][0], i+1);
				resultado = max(a,b);
			}
		}
	}
	guardado[comprimento_disponivel][i] = resultado;
	return resultado;
}

int main(){
	int i, j, total, teste = 1;
	scanf("%d %d", &comprimento_total, &quantidade_frases);
	while(quantidade_frases && comprimento_total){
		for(i = 0; i <= max(quantidade_frases,comprimento_total); i++)
			for(j = 0; j <= max(quantidade_frases,comprimento_total); j++)
				guardado[i][j] = 0;
		for(i = 0; i < quantidade_frases; i++)
			scanf("%d %d", &frases[i][0], &frases[i][1]);
		total = mochila(comprimento_total, 0);
		printf("Teste %d\n", teste);
		teste++;
		printf("%d\n\n", total);
		scanf("%d %d", &comprimento_total, &quantidade_frases);
	}
}
