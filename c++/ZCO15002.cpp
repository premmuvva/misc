#include<stack>
#include<iostream>
#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for (int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int main(){
    int a,j=1;
    in a ;
    long long int b[a],c=0;
    in c;
    for (int i =0;i<a;i++)
        in b[i];
    sort(b,b+a);
    f(i,a-1){
        for (;j<a;j++){
            if(b[j]-b[i]>=c){
                c+=((a-i-1)*(i+1)-(j-i));
                break;
            }
        }
    }
    pr c;
    return 0;
}
