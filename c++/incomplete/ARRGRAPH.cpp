#include<stack>
#include<iostream>
#include <bits/stdc++.h>
#include<vector>
#include<cmath>
#include<tr1/stdio.h>
using namespace std;
#define fo(i,a,b)  for(int i =a;i<b;i++)
#define f(i,x) for(int i=0; i<x; i++)
#define pr cout<<
#define in cin>>
int main(){
    int t,n,limit,ext,cou,a[50][2],compar[51]={0,0,256, 128, 256, 64, 384, 32, 256, 128, 320, 16, 384, 8, 288, 192, 256, 4, 384, 2, 320, 160, 272, 1, 384, 64, 264, 128, 288, 0, 448, 0, 256, 144, 260, 96, 384, 0, 258, 136, 320, 0, 416, 0, 272, 192, 257, 0, 384, 32, 320};
    scanf("%d",&t);
    while(t--){
        limit=1,ext=0,cou=2;
        scanf("%d",&n);
        f(i,n){
            scanf("%d",&a[i][0]);
            a[i][1]=0;
        }
        a[0][1]=1;
        fo(j,1,n){
            if (compar[a[j][0]]==0&&a[j][0]!=a[j-1][0]){
                pr 0<<endl;
                f(j,n)
                printf("%d ",a[j][0]);
                pr endl;
                ext=1;
                break;
            }
            if(compar[a[j][0]]&compar[a[0][0]])
                    a[j][1]=1;
        }
        if(ext==1)
            continue;
        f(i,n)
            if(a[i][1]==0){
                limit++;
                f(j,n)
                    if(compar[a[j][0]]&compar[a[i][0]])
                        a[j][1]+=cou;
                cou*=2;
            }
        // f(i,n)
        // pr a[i][1];
        // pr endl<<"limit "<<limit;
        int l,j;
        for(l=0;l<n;l++){
            if((pow(2,limit)-1)==a[l][1]){
                // pr endl<<"l "<<l<<endl;
                for(j=0;j<n;j++)
                    if(j!=l&&((compar[a[j][0]]&compar[a[l][0]])==0))
                    break;
                // pr endl;
                if(j==n){
                    pr 1<<endl;
                    f(j,n-1)
                    printf("%d ",a[j][0]);
                    // if(a[j][0]==47)
                    // pr 41<<endl;
                    // else
                    pr 47<<endl;
                    ext=1;
                    break;
                }
            }
        }
        if(ext==1)
            continue;
        // f(j,n)
        // pr compar[a[j][0]]<<" ";
        for(j=0;j<n-1;j++)
            if(compar[a[j][0]]!=0||a[j][0]!=a[j+1][0])
            break;
        if(j<n-1){
        pr 0<<endl;
        f(j,n)
            printf("%d ",a[j][0]);
        pr endl;
        }
        else{
            pr 1<<endl;
            f(j,n-1)
               printf("%d ",a[j][0]);
            if(a[j][0]==47)
            pr 41<<endl;
            else
            pr 47<<endl;
        }
    }
    return 0;
}
