#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a,cp=0,cc,av=0;
    scanf("%d",&a);
    long long int b[a],c;
    scanf("%lld",&c);
    for (int i =0;i<a;i++)
        scanf("%lld",&b[i]);
    while(true){
        scanf("%d",&cc);
        if(cc>0)
                switch (cc){
                case 1:
                    if(cp>0)
                        cp--;
                    break;
                case 2:
                    if(cp<a-1)
                        cp++;
                    break;
                case 3:
                    if (av==1||b[cp]==0)
                        break;
                    b[cp]--;
                    av=1;
                    break;
                case 4:
                    if(av==0||b[cp]>=c)
                        break;
                    b[cp]++;
                    av=0;
                    }

        else
            break;
        }
        for (int i=0;i<a;i++)
    printf("%lld ",b[i]);
}

