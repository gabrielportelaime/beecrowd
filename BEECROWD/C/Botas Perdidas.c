#include <stdio.h>

int min (a, b) {
	if(a < b)
		return a;
	return b;
}

int main(){
	int i, n, cont, pares[31][2], tamanho;
	char pe;
	while(scanf("%d", &n) != EOF){
		cont = 0;
		memset(pares, 0, sizeof(pares));
		for(i = 0; i < n; i++){
			scanf("%d %c", &tamanho, &pe);
			if(pe == 'D')
				pares[tamanho-30][0]++;
			else
				pares[tamanho-30][1]++;
		}
		for(i = 0; i < 31; i++)
			cont += min(pares[i][0], pares[i][1]);
		printf("%d\n", cont);
	}
}
