#include<stack>
#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<cmath>

using namespace std;

#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
#define sc(arg2) scanf("%d",&arg2);
#define nl printf("\n");

int main(){
    int t,n,m,a[100],b[100];
    long long int sa,sb;
    sc(t)
    while (t--){
        sa=0;sb=0;
        scanf("%d%d",&n,&m);
        f(i,n){
        sc(a[i]);
        sa+=a[i];
        if(a[i]==0){
            i--;n--;
        }
        }
        f(i,m){
        sc(b[i]);
        sb+=b[i];
        if(b[i]==0){
            i--;m--;
        }
        }
        if(sa==sb&&n==m){
            int flag=1;
            sort(a,a+n);
            sort(b,b+m);
            f(i,n)
            if(a[i]!=b[i])
            flag=0;
            if(flag==1)
            pr "Bob";
            else
            pr "Alice";
        }
        else
        pr "Alice";
        nl
    }
    return 0;
}
