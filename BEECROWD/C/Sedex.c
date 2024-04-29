#include <stdio.h>

int main(void) {
	int a,b,c,d;
	scanf("%d", &d); 
	scanf("%d %d %d", &a, &b, &c);
	if(d >= a && d >= b && d >= c)
		printf("S");
	else
		printf("N");
	return 0;
}
