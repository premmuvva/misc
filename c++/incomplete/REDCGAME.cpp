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
    long int t,n,k,a[50],sum,j,temp;
    scanf("%d",&t);
    while(t--){
        sum=0;
        scanf("%ld %ld",&n,&k);
        f(j,n)
            scanf("%ld",&a[j]);
        sort(a,a+n);
        for(j=0;j<n-1;j++){
            if(a[j]>k)
            break;
            sum+=a[j];
        }
        for (int i=j;i<n-1;i++){
            if(a[i]>k){
                temp=a[i];
                a[i]=(a[i]%(k)==0)?k:a[i]%(k);
                a[i+1]-=(temp-a[i]);
            }
            sum+=a[i];
        }
        printf("%d\n", sum+a[n-1]);
    }
    return 0;
}
