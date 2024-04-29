#include <iostream>
#include <vector>
using namespace std;

void kadane(vector<int>& vet)
{
	int max_atual;
	int max_total = -1;
	int posicao_inicial,posicao_final;
	int tam_periodo;

	for(int i = 0; i < vet.size(); i++)
	{
		max_atual = 0;
		for(int j = i; j < vet.size(); j++){
			tam_periodo = j-i;
			max_atual += vet[j];

			if(max_atual == max_total){
				if(tam_periodo > (posicao_final - posicao_inicial)){
					posicao_inicial = i+1;
					posicao_final = j+1;
				}
			}

			if(max_atual > max_total){
				max_total = max_atual;

				posicao_inicial = i+1;
				posicao_final = j+1;
			}

		}
	}

	
	if(max_total <= 0)
		cout << "nenhum" << endl;
	else
		cout << posicao_inicial << " " << posicao_final << endl;
}

int main(){
	int N,X,Y;
	vector<vector<int>> saldo_partida;
	int k=0;

	do{
		scanf("%d", &N);

		for(int i = 0; i<N; i++){
			saldo_partida.resize(k+1);

			scanf("%d %d",&X,&Y);
		
			saldo_partida[k].push_back(X-Y);
		} 
		k++;

	}while(N!=0);

	for(int i = 0; i<saldo_partida.size(); i++){
		cout << "Teste " << i+1 << endl;
		kadane(saldo_partida[i]);
		cout << endl;

	}

	return 0;
}
