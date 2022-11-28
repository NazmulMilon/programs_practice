#include<bits/stdc++.h>
using namespace std;


int main()
{
    int n,e;
    cin>>n>>e;

    int a,b, cnt=0;

    int arr[e], arr2[e];
    for(int i=0; i<e; i++)
    {
        // int a,b;
        cin>>arr[i]>>arr2[i];
    }

    // memset(visit, false, sizeof(visit));
    // cout<<endl<<endl;
    // bfs(1);
    int k;
    cin>>k;

    for(int i=0; i<e; i++)
    {
        //cout<<arr[i]<<" "<<arr2[i]<<endl;
        if(arr[i]==k)
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
2



6 5
0 1
0 2
0 3
2 3
4 5
2
*/

