#include<stdio.h>
main(){
    char s,c[100];
    printf("enter the string");
    getc(s);
    int i=0;
    while(s!='\n'){
        switch (s)
        {
            case 'a':
                c[i++]='a';
                break;

            case 'b':
                c[i++]='a';
                break;



            default:
                break;

        }
    }
}
