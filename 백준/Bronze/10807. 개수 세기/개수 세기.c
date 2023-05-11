#include<stdio.h>
int main(){
    int n, find_num,cnt=0;
    scanf("%d",&n);
    int li[n];
    for(int i=0;i<n;i++){
        scanf("%d",&li[i]);
    }
    scanf("%d",&find_num);
    for(int j=0;j<n;j++){
        if(li[j]==find_num)
        {
            cnt+=1;
        }
        
    }printf("%d",cnt);
}