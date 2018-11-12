#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
#include<tr1/stdio.h>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int arr[2][31][31][31][2][30];
int number_of_1s(int a){
    int result=0;
    while(a>0){
        if(a%2==1)
        result++;
        a/=2;
    }
    return result;
}
int count(int c,int a ,int b , int carry, int dif,int c1){
    if (a>b){
        int d=a;
        a=b;
        b=d;
    }
    if(a>-1&&b>-1&&dif>-1)
    if((arr[a][b][carry][dif])!=-1)
        return (arr[a][b][carry][dif]);
    if (dif<0||a<0||b<0||c1<0)
        return 0;
    if (c==0||c1==0){
        if(a==0&&b==0&&dif==0)
            return 1;
        return 0;
    }
    // if(a==0||b==0){
    //     if (c1==a+b)
    //         return 1;
    //     return 0;
    // }
    // if(a+b<c1)
    // return 0;
    // if (arr[c1][a][b][carry][dif]>-1)
    //     return arr[c1][a][b][carry][dif];
    if (c%2==0){
        if(carry == 0)
            arr[a][b][carry][dif]= count(c/2,a-1,b-1,1,dif-1,c1)+count(c/2,a,b,0,dif,c1);
        else
            arr[a][b][carry][dif]= count(c/2,a,b-1,1,dif-1,c1)+count(c/2,a-1,b,1,dif-1,c1);
    } 
    else{
        if(carry == 0)
            arr[a][b][carry][dif]= count(c/2,a,b-1,0,dif,c1-1)+count(c/2,a-1,b,0,dif,c1-1);
        else
            arr[a][b][carry][dif]= count(c/2,a,b,0,dif,c1-1)+count(c/2,a-1,b-1,1,dif-1,c1-1);
    }
    return arr[a][b][carry][dif];
}
int main(){
    int t,a=9,b,c;
    scanf("%d",&t);
    while(t--){
        f(ut,2)
        f(i,31)
            f(j,31)
                f(k,31)
                    f(l,2)
                        f(m,30)
                            arr[ut][i][j][k][l][m]=-1;
        scanf("%d %d %d",&a,&b,&c);
        a= number_of_1s(a);
        b= number_of_1s(b);
        int c1=number_of_1s(c);
        pr count(c,a,b,0,a+b-number_of_1s(c),c1)<<endl;
        // f(i,31)
        //     f(j,31)
        //         f(k,31)
        //             f(l,2)
        //                 f(m,30)
        //                 if(arr[i][j][k][l][m]>-1)
        //                    pr  arr[i][j][k][l][m]<<" ";

    }
    return 0;
}
