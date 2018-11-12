#include<bits/stdc++.h>
#define mod 1000000007
#define inf 3005
#define max 200005
using namespace std;
typedef  long long int ll;
template<typename T> inline T maxi(T a,T b){return a>b?a:b;}
template<typename T> inline T mini(T a,T b){return a<b?a:b;}
template<typename T> inline T absl(T a){return a>0?a:-a;}
template<typename T> inline T gcd(T a,T b){T t;if(a<b){while(a){t=a;a=b%a;b=t;}return b;}else{while(b){t=b;b=a%b;a=t;}return a;}}
#define mp(a,b) make_pair(a,b)
//###################################################------------------------------------------------------#######################################


void input(){
   int t;
   cin>>t;
   while(t--){
    ll n,m,x,y;
    scanf("%lld%lld%lld%lld",&n,&m,&x,&y);
    ll l=0,r=0,ans=0;
    l=(y-1>=1)?y-1:0;
    r=(m-y>=1)?r=m-y:0;
    ans+=(l*r);
    l=(x-1>=1)?x-1:0;
    r=(n-x>=1)?r=n-x:0;
    ans+=(l*r);
    l=((x-1>=1)&&(m-y>=1))?(mini(x-1,m-y)):0;
    r==((n-x>=1)&&(y-1>=1))?(mini(n-x,y-1)):0;
     ans+=(l*r);
    l=((x-1>=1)&&(y-1>=1))?(mini(x-1,y-1)):0;
    r=((n-x>=1)&&(m-y>=1))?(mini(n-x,m-y)):0;
    ans+=(l*r);
   // cout<<ans<<endl;
    ll ans2=0;
    for(ll i=1;i<=n;++i){
        for(ll j=1;j<=m;++j){
            ll l1=((i-1>=1)&&(m-j>=1))?(mini(i-1,m-j)):0;
    ll r1=((n-i>=1)&&(j-1>=1))?(mini(n-i,j-1)):0;
    ll l2=((i-1>=1)&&(j-1>=1))?(mini(i-1,j-1)):0;
   ll r2=((n-i>=1)&&(m-j>=1))?(mini(n-i,m-j)):0;//cout<<l1<<" "<<r1<<" "<<l2<<" "<<r2<<endl;
   ll p=l1+l2+r1+r2+(m-1)+(n-1)+1;
     ans2+=((n*m)-p>=0)?(n*m)-p:0;//cout<<(n*m)-p<<endl;
        }
    } //cout<<ans2<<endl;
    //cout<<ans2<<endl;
     ll l1=((x-1>=1)&&(m-y>=1))?(mini(x-1,m-y)):0;
    ll r1=((n-x>=1)&&(y-1>=1))?(mini(n-x,y-1)):0;
    ll l2=((x-1>=1)&&(y-1>=1))?(mini(x-1,y-1)):0;
   ll r2=((n-x>=1)&&(m-y>=1))?(mini(n-x,m-y)):0;
   ll p=l1+l2+r1+r2+(m-1)+(n-1)+1;
   ans2-=(2*((n*m)-p)>=0)?(2*((n*m)-p)):0;//cout<<2*((n*m)-p)<<endl;

    printf("%lld\n",(2*ans+ans2));
   // cout<<ans<<endl;
   }
}

int main(){
  input();
  return 0;
}