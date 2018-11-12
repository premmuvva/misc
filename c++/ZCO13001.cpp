#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    long long int a;
    scanf("%lld",&a);
    long long int b[a],c=0;
    for (int i =0;i<a;i++)
        scanf("%lld",&b[i]);
    sort(b,b+a);
    for (int i =0;i<a-1;i++)
        c+=(b[i+1]-b[i])*(a-i-1)*(i+1);
    printf("%lld\n",c);
}

