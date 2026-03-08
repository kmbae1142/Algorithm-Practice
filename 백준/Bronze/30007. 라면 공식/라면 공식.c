#include <stdio.h>

int main() {
    
    int A, B, X;
    int num;
    
    scanf("%d", &num);
    
    for (int i = 0; i < num; i++) {
        scanf("%d %d %d", &A, &B, &X);
        printf("%d\n", A * (X - 1) + B);
    }
    
}