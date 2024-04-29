#include <stdio.h>
#define Dim 105

int transmissoes[Dim][Dim] = {0}, vis[Dim] = {0}, cidades, linhas;

void dfs(int x){
	int i;
	vis[x] = 1;
 	for(i = 1; i <= cidades; i++) 
 		if(transmissoes[x][i] && !vis[i])
	 		dfs(i);
}

int main(){
	int i, j, v1, v2, normal = 1, teste = 1;
	scanf("%d %d", &cidades, &linhas);
	while(cidades != 0 && linhas != 0){
		for(i = 0; i < linhas; i++){
			scanf("%d%d", &v1, &v2);
			transmissoes[v1][v2] = 1;
			transmissoes[v2][v1] = 1;
		}
		dfs(1);
		for(i = 1; i <= cidades; i++){
			if(vis[i] == 0){
				normal = 0;
				break;
			}
		}
		printf("Teste %d\n", teste);
		teste++;
		if(normal)
			printf("normal\n\n");
		else
			printf("falha\n\n");
		scanf("%d %d", &cidades, &linhas);
		for(i = 1; i < Dim; i++)
			vis[i] = 0; 
		for(i = 1; i < Dim; i++)
			for(j = 1; j < Dim; j++)
				transmissoes[i][j] = 0; 
		normal = 1;
	}
}
