#include <stdio.h>

int chamadas;

int fibo(int n){
	chamadas++;
	if(n == 1 || n == 0)
		return n;
	return fibo(n-1)+fibo(n-2);
}

int main(){
	int i, n, resultado, vezes;
	scanf("%d", &vezes);
	for(i = 0; i < vezes; i++){
		scanf("%d", &n);
		chamadas = -1;
		resultado =  fibo(n);
		printf("fib(%d) = %d calls = %d\n", n, chamadas, resultado);
	}
}
