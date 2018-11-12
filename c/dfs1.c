#include<stdio.h>
main(){
    char c[500]="";
    int i =0;
    while(i<50){
        printf("%s\n",c);
        c[i++]='a';
    }
}
