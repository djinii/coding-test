#include<stdio.h>
#include<math.h>

int main(){
    int n,a,b;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&a,&b);
        a=a%10;
        if(a==0){
            printf("10\n");
        }else{
            b=(b%4)+4;
            double re=pow(a,b);
            re=fmod(re,10.0);
            printf("%d\n", (int)re);
        }
    }
}