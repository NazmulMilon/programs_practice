#include<bits/stdc++.h>
using namespace std;

typedef pair <int, int> edgeWeightPair;
class Graph
{
    int V;
    list <edgeWeightPair> *adj;
public:
    Graph(int V)
    {
        this->V = V;
        adj = new list<edgeWeightPair> [V];
    }

    // void addEdge(int u, int v)
    // {
    //     adj[u].push_back(make_pair(v, u));
    //     adj[v].push_back(make_pair(u, v));
    // }

    void printNeighbour(int chk)
    {
        cout<<chk<< ":";
        for(auto i=adj[chk].begin(); i!= adj[chk].end(); i++)
        {
            cout<<" (" << (*i).first <<", "<<(*i).second<<")";
        }
    }

};

int main()
{
    int V, E;
    cin>>V>>E;

    int u,v;
    Graph g(V);
    for(int i=0; i<E; i++)
    {

        cin>>u>>v;
        //g.addEdge(u, v);
    }

    int k;
    cin>>k;

    int cnt=0;
    for(int i=0; i<V; i++)
    {
    //     g.printNeighbour(i);
    //     cout<<endl;
    // }
        if(u==k || v==k)
        {
            cnt++;
        }
    }
    cout<<cnt<<endl;
    return 0;
}

/*
6 5
0 1
0 2
0 3
2 3
4 5



Bi-Directional Weighted Graph
7 10
0 1 7
0 2 1
0 5 3
1 3 11
2 3 3
3 6 1
6 5 2
6 4 4
5 4 6
2 5 8



*/
