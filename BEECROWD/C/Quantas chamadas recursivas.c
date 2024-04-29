#include <stdio.h>

int main(){
	long long int numero;
	int i, j, caso = 1, base, chamadas[100005];;
	scanf("%lld %d", &numero, &base);
	chamadas[0] = chamadas[1] = 1;
	while(numero || base){
		for(i = 2; i < 100001; i++){
			chamadas[i] = (chamadas[i-1] +chamadas[i-2] + 1)%base;
			if(chamadas[i] == 1 && chamadas[i-1] == 1)
				break;
		}
		i--;
		printf("Case %d: %lld %d %d\n", caso, numero, base, chamadas[numero%i]);
		caso++;
		scanf("%lld %d", &numero, &base);
	}
}	
