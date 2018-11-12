#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
#include<string>
#include<cstdio>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int t,h1,w1,h2,w2;
string s1,s2;
/*
1
3 2
011011
2 3
100101
*/
long int cal1(int a,int b)
{
    long int l= (h1*h2)/__gcd(h1,h2),a1,a2,cou=0,complete=0;
        a1=l/h1;
        a2=l/h2;
        for(int i1 =1,j=1;complete<l;){
            if(s1[a*w1-w1+i1]==s2[b*w2-w2+j])
                cou+=(min(i1*a1,j*a2)-complete);
            complete=min(i1*a1,j*a2);
            if(i1*a1<=j*a2)
                i1++;
            else
                j++;
        }
    //pr cou<<a<<b<<"\n";
    return cou;
}
long int cal(int a,int b)
{
    long int l= (h1*h2)/__gcd(h1,h2),a1,a2,cou=0,complete=0;
        a1=l/h1;
        a2=l/h2;
        for(int i1 =1,j=1;complete<l;){
            cou+=(min(i1*a1,j*a2)-complete)*(s1[i1*w1-w1+a]^s2[j*w2-w2+b]);
            complete=min(i1*a1,j*a2);
            if(i1*a1<=j*a2)
                i1++;
            else
                j++;
        }
    //pr cou<<a<<b<<"\n";
    return cou;
}
int main(){
    in t;
    int a1,a2,l;
    f(i,t){
        long int complete=0,cou=0;
        in h1>>w1>>s1;
        in h2>>w2>>s2;
        l= (w1*w2)/__gcd(w1,w2);
        a1=l/w1;
        a2=l/w2;
        for(int i1 =1,j=1;complete<l;){
            cou+=(min(i1*a1,j*a2)-complete)*cal(i1-1,j-1);
            complete=min(i1*a1,j*a2);
            if(i1*a1<=j*a2)
                i1++;
            else
                j++;
        }
        pr l*(h1*h2)/__gcd(h1,h2)-cou<<endl;
    }
    return 0;
}
