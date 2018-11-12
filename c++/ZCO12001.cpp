#include<stack>
#include<iostream>
#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for (int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int main(){
    int a,b,t;
    in a;
    int ar[2][a];
    in ar[0][0];
    ar[1][0]=ar[0][0];
    fo(i,1,a){
        in ar[0][i];
        if ( ar[0][i]==2)
            ar[0][i]=-1;
        ar[1][i]=ar[0][i]+ar[1][i-1];
    }
    int maxi=0,mi=0,ii=0,gi=0,gco=0;
    f(i,a){
        if (ar[1][i]>maxi) {
            maxi=ar[1][i];
            mi=i+1;
        }
        else if(ar[1][i]==0){
            if(i-ii+1>gco){
                gco=i-ii+1;
                gi=ii+1;
            }
            ii=i+1;
        }
    }
    pr maxi<< " "<< mi <<  " "<< gco << " "<< gi<<"\n";
    return 0;
}
