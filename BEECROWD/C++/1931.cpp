#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MAXN 10100
#define INF 0x3f3f3f3f
typedef pair<int,int> par;
vector<par> lista[MAXN];
int c, v;
int dijkstra(int origem, int destino){
	par dist[MAXN];
	for(int i = 1; i <= c; i++) dist[i]=par(INF,INF);
	dist[1]=par(0,INF);
	priority_queue<par, vector<par>, greater<par>> heap;
	heap.push(par(0, 1));
	while(!heap.empty()){
		int v = heap.top().S, d = heap.top().F; heap.pop();
		if(d > dist[v].F and d > dist[v].S) continue;
		for(int i = 0; i < lista[v].size(); i++){
			par u=lista[v][i];
			if(dist[v].F+u.S<dist[u.F].S){
				dist[u.F].S=dist[v].F+u.S;
				heap.push(par(dist[u.F].S, u.F));
			}
			if(dist[v].S+u.S<dist[u.F].F){
				dist[u.F].F=dist[v].S+u.S;
				heap.push(par(dist[u.F].F, u.F));
			}
		}
	}
	if(dist[destino].F == INF) return -1;
	return dist[destino].F;
}		

int main(){
	scanf("%d %d", &c, &v);
	for(int i=1; i<=v; i++){
		int c1, c2, g;
		scanf("%d %d %d", &c1, &c2, &g);
		lista[c1].PB(par(c2,g));
		lista[c2].PB(par(c1,g));
	}
	printf("%d\n", dijkstra(1,c));
	return 0;
}