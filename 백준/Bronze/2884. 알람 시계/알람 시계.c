#include<stdio.h>
int main(){
    int h,m,al_h,al_m;
    scanf("%d %d",&h,&m);
    al_m=m-45;
    al_h=h;
    if(al_m<0){
        al_m+=60;
        al_h=h-1;
        if(al_h<0){
            al_h+=24;
        }
    }printf("%d %d",al_h,al_m);
    return 0;
}