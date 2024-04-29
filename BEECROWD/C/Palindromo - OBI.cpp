#include <iostream>
#include <string>
#include <math.h>

#define Dim 2005
#define INF 999999

using namespace std;

int matriz[Dim][Dim], n, distancia[Dim], fila[Dim], k, andado;

string palavra;

int menor_caminho(int vertice){
	for(int i = vertice; i < n; i++){
		if(matriz[vertice][i] && distancia[i+1] == -1){
			distancia[i+1] = distancia[vertice] + 1;
			if(i+1 == n){
				return distancia[n]; 
			}else{
				fila[k] = i+1;
				k++;
			}
		}
	}
	andado++;
	return menor_caminho(fila[andado]);
}

int main(){
	int bla;
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	cin >> palavra;
	for(int i = 0; i <= n; i++)
		distancia[i] = -1;
	distancia [0] = 0;
	for(int i = 0; i < n; i++)
    	for(int j = 0; j < n; j++) 
			matriz[i][j] = (i == j) ? 1 : 0;
    for(int i = 0; i < n; i++){
      	int x = 0;
      	while(i-x >= 0 and i+x+1 < n and palavra[i-x] == palavra[i+x+1]) matriz[i-x][i+x+1] = 1, x++;
      	x = 0;
      	while(i-x-1 >= 0 and i+x+1 < n and palavra[i-x-1] == palavra[i+x+1]) matriz[i-x-1][i+x+1] = 1, x++; 
    }
	k = 1;
	andado = 0;
	fila[0] = 0;
	cout << menor_caminho(0);
	return 0;
}
