#include<bits/stdc++.h>
using namespace std;

#define ll long long
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll i,j,l,u,k,max=0, cnt=0;
        cin>>l>>u;
        if(u<l)
        {
            ll temp = l;
            l = u;
            u = temp;
        }
        for(i = l; i<=u; i++)
        {
            cnt = 0;
            for(j=1; j<=i; j++)
            {
                if(i%j == 0){
                    cnt++;
                }
            }
            if(cnt>max){
                max = cnt;
                k = i;
            }
        }
        cout<<"Between "<<l<<" and "<<u<<", "<<k<<" has a maximum of "<<max<<" divisors. "<<endl;
    }
    return 0;
}

'''
#define ll long long;
int main()
{
    int t;
    cin>>t;
    int l, u;
    while(t--)
    {
        cin>>l>>u;
        int sum = -1;
        int su;
        for(int i=l; i<=u; i++)
        {
            int ans = l;
            int ii=i;
            for(int j=2; j*j<=ii; j++)
            {
                if(ii%j == 0)
                {
                    int cnt = 1;
                    while(ii%j == 0){
                        cnt++;
                        ii=ii/j;
                    }
                    ans*=cnt;
                }
            }
            if(ii>1){
                ans*=2;
            }
            if(ans>sum)
            {
                sum=ans;
                su = i;
            }
        }
        cout<<"Between "<<l<<" and "<<u<<", "<<su<<" has a maximum of "<<sum<<" divisors. "<<endl;
    }
    return 0;

}
'''