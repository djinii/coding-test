#include<stdio.h>
int main(){
    int h, m, c_t,quotient,remainder;
    scanf("%d %d",&h,&m);
    scanf("%d",&c_t);
    m+=c_t;
    quotient=m/60;
    remainder=m%60;
    if(remainder==0){
        if(remainder>=60){
            m=m-(60*quotient);
        }else{
            m=0;
        }
    }else{
        m=m-(60*quotient);
    }
    h+=quotient;
    if(h>23){
        h-=24;
    }
    printf("%d %d",h,m);
    return 0;
}