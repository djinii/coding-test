#include<stdio.h>
int main(){
    int a,b,c,m;
    scanf("%d %d %d",&a,&b,&c);
    if(a==b){
        if(b==c){
            m=10000+(a*1000);
        }else{
            m=1000+(a*100);
        } 
    }else{
        if(b==c){
            m=1000+(b*100);
        }else if(a==c){
            m=1000+(a*100);
        }else if(a>b){
            if(a>c){
                m=a*100;
            }else{
                m=c*100;
            }
        }else{
            if(b>c){
                m=b*100;
            }else{
                m=c*100;
            }
        }   
    }
    printf("%d",m);
    return 0;
}