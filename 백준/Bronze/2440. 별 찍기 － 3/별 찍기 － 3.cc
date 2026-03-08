#include <stdio.h>

int main() {

    int num;
    int i, j;
    scanf("%d", &num);

    for (i = num; i > 0; i--) {
        
        for (j = i; j > 0; j--) {
            printf("*");
        }
        printf("\n");
        
    }
}