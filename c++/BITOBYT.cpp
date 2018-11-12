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
int main(){
    long int t,n;
    in t;
    f(i,t){
        in n;
        if (n%26==0&&n>0)
           pr "0 0 "<<(long int )(pow(2,(n/26)-1)+.5)<< endl;
        else if (n%26<3)
            pr (long int )(pow(2,(n/26))+.5)<< " 0 0"<<endl;
        else if(n%26<11)
            pr "0 "<<(long int )(pow(2.0,(n/26))+.5)<< " 0"<<endl;
        else
            pr "0 0 "<<(long int )(pow(2.0,(n/26))+.5)<< endl;
    }
    return 0;
}
