#include <stdio.h>

int main() {

    int num;
    int i, j, k;
    scanf("%d", &num);

    for (i = 0; i < num; i++) {
        for (j = i; j > 0; j--) {
            printf(" ");
        }
        for (k = num; k > i; k--) {
            printf("*");
        }
        printf("\n");
    }
}