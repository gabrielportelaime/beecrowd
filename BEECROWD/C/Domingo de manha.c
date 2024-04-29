#include <stdio.h>

int main(){
	int hora, minutos, atraso;
	char horas[4];
	while(scanf("%s", &horas)!=EOF){
		hora = (int)(horas[0]) - (int)('0');
		minutos = ((int)(horas[2]) - (int)('0'))*10 + (int)(horas[3]) - (int)('0'); 
		atraso = 0;
		atraso += (8 - hora)*60 - minutos;
		if(atraso > 60)
			printf("Atraso maximo: 0\n");
		else
			printf("Atraso maximo: %d\n", 60-atraso);	
	}
}
