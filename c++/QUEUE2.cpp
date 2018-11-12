#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
#include<cmath>

using namespace std;

#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
#define sc(arg2) scanf("%llu",&arg2);
#define nl printf("\n");
#define sp printf("     ");

int main(){
    signed long long int t,n,m,k,l,a[100000],b[100000],min;
    sc(t)
    while(t--){
        scanf("%llu%llu%llu%llu",&n,&m,&k,&l);
        f(i,n)
            sc(a[i]);
        sort(a,a+n);
        if (m*l+l>=a[0])    b[0]=m*l+l;
        else    b[0]=a[0];
        min = m*l+l-a[0];
        fo(i,1,n){
            if(a[i]-b[i-1]<=l)  b[i]=b[i-1]+l;
            else    b[i] =a[i] ;
            
            if(min>b[i] -a[i])     min=b[i] -a[i] ;
        }
        if(min<0)
        min=0;
        if(k<b[n-1]+l){
            if(b[n-1] -k+l<min)
            pr b[n-1]-k+l;
            else 
            pr min;
        }
        else    pr 0;
        nl
    }
    return 0;
}
