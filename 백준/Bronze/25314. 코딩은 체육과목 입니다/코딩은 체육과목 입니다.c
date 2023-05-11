#include<stdio.h>
int main(){
    int n, repeat;
    scanf("%d",&n);
    repeat=n/4;
    for(int i=0;i<repeat;i++){
        printf("long ");
    }
    printf("int");
}