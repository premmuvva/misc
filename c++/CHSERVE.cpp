#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int main(){
    int t,p1,p2,k;
    in t;
    f(i,t){
        in p1>>p2>>k;
        if(((p1+p2)/k)%2==0)
            pr "CHEF"<<endl;
        else
            pr "COOK"<<endl;
    }
    return 0;
}
