#include<stdio.h>
#include <stdbool.h>

int main(){
    int students[28];
    int N_students[31];
    for(int i = 0; i < 28; i++){
        scanf("%d", &students[i]); 
    }
    for (int q = 1; q<31; q++){
        N_students[q] = 55;
        for (int j = 0; j < 28; j++) {
            if(q == students[j]){
                N_students[q]=q;
            }
        }
    }
    int n = sizeof(N_students) / sizeof(N_students[0]);
    // printf("result is %d %lu %lu\n", n, sizeof(N_students), sizeof(N_students[0]));

    for (int a = 1; a <= 30; a++) {
        bool found = false;
        for (int b = 1; b <= 30; b++) {
            if (N_students[b] == a) {
                found = true;
                break;
            }
        } 
        if (!found) {
            printf("%d\n", a);
        }
    }

    return 0;
}
