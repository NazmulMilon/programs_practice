#include<bits/stdc++.h>
using namespace std;

vector<int> v[100];
bool visit[100];

void bfs(int src, int k)
{
    queue<pair<int, int>> q;
    q.push({src,0});

    int cnt=0;
    while(!q.empty())
    {
        pair<int ,int> parent = q.front();
        q.pop();

        if(visit[parent.first]==true) continue;
        //cout<<parent.first<<" "<<parent.second<<endl;
        if(parent.second==k)
        {
            cnt++;
        }

        for(int i=0; i<v[parent.first].size(); i++)
        {
            int children = v[parent.first][i];
            if(visit[children] == false) q.push({children, parent.second+1});
        }
        visit[parent.first] = true;
    }
    cout<<cnt<<endl;
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
        v[b].push_back(a);
    }
    
    int k;
    cin>>k;

    memset(visit, false, sizeof(visit));
    //cout<<endl<<endl;
    bfs(1, k);
    return 0;
}


/*
6 7
5 3
4 5
1 0
1 2
1 3
3 0
4 3



















6 5
0 1
0 2
0 3
2 3
4 5
2
*/
