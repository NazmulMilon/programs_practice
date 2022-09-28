#include<bits/stdc++.h>
using namespace std;

vector<int> v[101];
bool visit[101];

void bfs(int src)
{
    queue<pair<int, int>> q;
    q.push({src,0});
    while(!q.empty())
    {
        pair<int ,int> parent = q.front();
        q.pop();

        if(visit[parent.first]==true) continue;
        cout<<parent.first<<" "<<parent.second<<endl;
        for(int i=0; i<v[parent.first].size(); i++)
        {
            int children = v[parent.first][i];
            if(visit[children] == false) q.push({children, parent.second+1});
        }
        visit[parent.first] = true;
    }
}

int cnt=0;
void DFS(int src)
{

    //cout<<src<<" ";
    cnt++;
    visit[src]=true;
    for(int i=0; i<v[src].size(); i++)
    {
        int children = v[src][i];
        if(visit[children] == false)
        {
            DFS(children);
            //cnt++;
        }
    }

    //cout<<endl<<cnt<<endl;
}

int main()
{
    int n,e;
    cin>>n>>e;

    for(int i=0; i<e; i++)
    {
        int a,b;
        cin>>a>>b;
        v[a].push_back(b);
        //v[b].push_back(a);
    }

    int k;
    cin>>k;
    memset(visit, false, sizeof(visit));
    //cout<<endl<<endl;
    DFS(k);
    //cout<<endl<<endl;

    if(cnt>1)   cout<<cnt-1<<endl<<endl;
    else cout<<"0"<<endl;
    
    return 0;
}


/*
7 7
1 2
1 6
2 3
2 4
6 4
6 7
4 5
2


6 5
0 1
0 2
2 3
3 0
4 5
2

6 5
0 1
0 2
0 3
2 3
4 5
6
*/