#include<stdio.h>
int main(){
    int total,cnt, won, quantity, sum=0;
    scanf("%d", &total);
    scanf("%d", &cnt);
    for(int i = 0; i < cnt; i++){
        scanf("%d %d", &won, &quantity);
        sum += (won * quantity);
    }
    if(sum == total){
        printf("Yes\n");
    }else{
        printf("No\n");
    }
}