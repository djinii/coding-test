#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
        for(int i=1;i<n+1;i++){
            for(int j=n-i;j>0;j--){
                printf(" ");
            }
            for(int q=1;q<i+1;q++){
                printf("*");
            }
            printf("\n");
        }
    return 0;
}