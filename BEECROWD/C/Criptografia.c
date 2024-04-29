#include <stdio.h>

char palavra[10001];

void primeiro(){
    int i;
    for(i = 0; i < strlen(palavra); i++)
        if((palavra[i] > 64 && palavra[i] < 91) || (palavra[i] > 96 && palavra[i] < 123))
            palavra[i] = palavra[i] + 3;
    segundo();
}

void segundo(){
    int i;
    char aux;
    for(i = 0; i < (strlen(palavra) + 1)/2; i++){
        aux = palavra[strlen(palavra) - i - 1];
        palavra[strlen(palavra) - i - 1] = palavra[i];
        palavra[i] = aux;
    }
    terceiro(palavra);
}

void terceiro(){
    int i;
    for(i = strlen(palavra)/2; i < strlen(palavra); i++)
        palavra[i]--;
    puts(palavra);
}

int main(){
    int i, n;
    scanf("%d ", &n);
    for(i = 0; i < n; i++){
        gets(palavra);
        primeiro();
    }
    return 0;
}
	
