#include<stdio.h>
int factorial(n){
    int r;
    r=1;
    if(n>1){
        r=n*factorial(n-1);
    }
    return r;

}

int main(){
    int n, result;
    scanf("%d",&n);
    
    result=factorial(n);
    printf("%d",result);

    return 0;
}