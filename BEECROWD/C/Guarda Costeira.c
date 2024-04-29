#include <stdio.h>
#include <math.h>

main(){
    int a, b, c;
    float xb;
    while(scanf("%d %d %d", &a, &b, &c) != EOF){
    	xb = sqrt(a*a+12*12);
    	if(((xb)/((float)(c))) <= ((12.0)/((float)(b))))
        	printf("S\n");
     	else
     		printf("N\n");
    }
}
