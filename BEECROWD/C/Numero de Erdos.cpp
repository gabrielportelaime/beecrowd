#include <bits/stdc++.h>
using namespace std;


const int INF = 999999;

int n, cnt;
string a;
map<string, int> ht;
map<string, vector<string>> adj;
vector<string> in;

bool cmp(string a, string b){
  if(a.substr(3) == b.substr(3)) return a[0] < b[0];
  return a.substr(3) < b.substr(3);
}

void get_nomes(string a){
  string name;
  vector<string> aux;
  for(int i = 0; i < a.size(); i++){//pega os nomes na linha
    if(a[i] == ',') {
    	aux.push_back(name);
    	in.push_back(name);
    	name = "";
    	i++;
    }
    else if(i == a.size() - 1) {
    	aux.push_back(name);
    	in.push_back(name);
    }
    else name += a[i];
  }

  for(auto x : aux)//coloca na lista de adjacencias dos vértices
    for(auto y : aux) 
    	if(x != y) adj[x].push_back(y);
}

void bfs(string s = "P. Erdos"){
  queue<pair<string, int>> q;
  q.push({s, 0});
  while(q.size()){
    string x = q.front().first;
    int h = q.front().second;
    q.pop();
    for(auto u : adj[x]) {
      if(ht[u] != INF) continue;//prox iteração
      ht[u] = h + 1;
      q.push({u, ht[u]});
    }
  }
}

int main(){

  while(cin >> n and n and ++cnt){
    ht.clear(), adj.clear(), in.clear(); 
    cin.ignore();
    
    while(n--) getline(cin, a), get_nomes(a);
    
    cout << "Teste " << cnt << "\n";
    sort(in.begin(), in.end(), cmp);
    in.resize(unique(in.begin(), in.end()) - in.begin());//retira os elementos consecutivos repetidos (já está com sort) e da um resize para n imprimir lixo
    
    for(auto x : in) ht[x] = INF;
    ht["P. Erdos"] = 0;
    bfs();
    
    for(auto x : in) {
      if(x == "P. Erdos") continue;
      if(ht[x] != INF) cout << x << ": " << ht[x] << "\n";
      else cout << x << ": infinito\n"; 
    }
    cout << "\n";
  }
}

